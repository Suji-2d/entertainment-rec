import pandas as pd
import numpy as np
import re
import random
from nltk.stem.porter import PorterStemmer


# Read data
movies_df=pd.read_csv("./data/movie/mymoviedb.csv", lineterminator='\n')


# synopsis alteration
ps = PorterStemmer()
def remove_splChar_normalizeWords(ss_line):
    word_list = []
    ss_line = re.sub('[^A-Za-z0-9]',' ', ss_line)
    #ss_line.replace('\n','')
    for word in ss_line.split():
        word_list.append(ps.stem(word))    
    return  " ".join(word_list)


#remove commas and creating new column
movies_df["Tags"] =  movies_df['Overview'].apply(remove_splChar_normalizeWords) + " " +[v.replace(',',' ') for v in movies_df['Genre']]

from sklearn.feature_extraction.text import TfidfVectorizer

#getting tfidf
tfv = TfidfVectorizer(min_df=3,  max_features=None, 
            strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
            ngram_range=(1, 3),
            stop_words = 'english')

# Filling NaNs with empty string
tfv_matrix = tfv.fit_transform(movies_df["Tags"])

from sklearn.metrics.pairwise import sigmoid_kernel

# Compute the sigmoid kernel
sig = sigmoid_kernel(tfv_matrix, tfv_matrix)

#getting the indices of anime title
indices = pd.Series(movies_df.index, index=movies_df['Title']).drop_duplicates()

def give_rec(title, sig=sig):
    # Get the index corresponding to original_title
    movieList=[]
    idx = indices[title]

    # Get the pairwsie similarity scores 
    sig_scores = list(enumerate(sig[idx]))

    # Sort the movies 
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

    same_mvi = [a for a in sig_scores if title in movies_df['Title'].iloc[a[0]]]
    diff_mvi = [a for a in sig_scores if a[0] not in [i for i,val in same_mvi]]
    s_len=len(same_mvi) if len(same_mvi)<4 else 3 
    # Scores of the 10 most similar movies
    sig_scores = same_mvi[1:s_len] + diff_mvi[:(11-s_len)]

    for i in sig_scores:      
        movieList.append([movies_df.iloc[i[0]]["Title"],f'{movies_df.iloc[i[0]]["Vote_Average"]:.1f}'])  
    return  movieList

def getAllTitlesAvailable():
    return list(movies_df['Title'])

#get rangom anime title and rationg from top ranked
def getRandomSuggestion(n):
    return random.sample(list(movies_df[movies_df['Vote_Average']>7]['Title']), n)

