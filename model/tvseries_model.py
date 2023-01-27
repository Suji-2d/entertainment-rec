import pandas as pd
import numpy as np
import re
import random
from nltk.stem.porter import PorterStemmer


# Read data
series_df=pd.read_csv("./data/movie/tvseries.csv")


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
series_df["Tags"] =  series_df['genres'] + " " +[v.replace(',',' ') for v in series_df['directors']] + " " + [v.replace(',',' ') for v in series_df['actors']] + " " +[v.replace(',',' ') for v in series_df['writers']]

from sklearn.feature_extraction.text import TfidfVectorizer

#getting tfidf
tfv = TfidfVectorizer(min_df=3,  max_features=None, 
            strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
            ngram_range=(1, 3),
            stop_words = 'english')

# Filling NaNs with empty string
tfv_matrix = tfv.fit_transform(series_df["Tags"])

from sklearn.metrics.pairwise import sigmoid_kernel

# Compute the sigmoid kernel
sig = sigmoid_kernel(tfv_matrix, tfv_matrix)

#getting the indices of anime title
indices = pd.Series(series_df.index, index=series_df['originalTitle']).drop_duplicates()

def give_rec(title, sig=sig):
    # Get the index corresponding to original_title
    movieList=[]
    idx = indices[title]

    # Get the pairwsie similarity scores 
    sig_scores = list(enumerate(sig[idx]))

    # Sort the movies 
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)[1:11]

    for i in sig_scores:      
        movieList.append([series_df.iloc[i[0]]["originalTitle"],f'{series_df.iloc[i[0]]["averageRating"]:.1f}'])  
    return  movieList

def getAllTitlesAvailable():
    return list(series_df['originalTitle'])

#get rangom anime title and rationg from top ranked
def getRandomSuggestion(n):
    return random.sample(list(series_df[series_df['averageRating']>7]['originalTitle']), n)

