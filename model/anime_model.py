import pandas as pd
import numpy as np
import re
import random
from nltk.stem.porter import PorterStemmer


# Read data
new_ani=pd.read_csv("./data/clean_data/anime.csv")

from sklearn.feature_extraction.text import TfidfVectorizer

#getting tfidf
tfv = TfidfVectorizer(min_df=3,  max_features=None, 
            strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
            ngram_range=(1, 3),
            stop_words = 'english')

# Filling NaNs with empty string
tfv_matrix = tfv.fit_transform(new_ani["Tags"])

from sklearn.metrics.pairwise import sigmoid_kernel

# Compute the sigmoid kernel
sig = sigmoid_kernel(tfv_matrix, tfv_matrix)

#getting the indices of anime title
indices = pd.Series(new_ani.index, index=new_ani['English']).drop_duplicates()

def give_rec(title, sig=sig):
    # Get the index corresponding to original_title
    movieList=[]
    idx = indices[title]

    # Get the pairwsie similarity scores 
    sig_scores = list(enumerate(sig[idx]))

    # Sort the movies 
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)
    
    same_anime = [a for a in sig_scores if title in new_ani['English'].iloc[a[0]]]
    diff_anime = [a for a in sig_scores if a[0] not in [i for i,val in same_anime]]
    s_len=len(same_anime) if len(same_anime)<4 else 3 
    # Scores of the 10 most similar movies
    sig_scores = same_anime[1:s_len] + diff_anime[:(11-s_len)]

    # Movie indices
    anime_indices = [i[0] for i in sig_scores]

    for i in sig_scores:      
        movieList.append([new_ani.iloc[i[0]]["English"],f'{new_ani.iloc[i[0]]["Score"]:.1f}'])  
    return  movieList

def getAllTitlesAvailable():
    return list(new_ani['English'])

#get rangom anime title and rationg from top ranked
def getRandomSuggestion(n):
    return random.sample(list(new_ani['English'])[:300], n)





