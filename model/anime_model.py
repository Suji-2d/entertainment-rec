import pandas as pd
import numpy as np
import re
import random
from nltk.stem.porter import PorterStemmer


# Read data
anime_d=pd.read_csv("./data/anime/anime_2022.csv")

new_ani = anime_d.drop(['ID',
 
 'Synonyms',
 'Japanese',
 'Premiered',
 'Broadcast',
 'Licensors',
 'Type',
 'Episodes',
 'Status',
 'Start_Aired',
 'End_Aired',
 'Duration_Minutes',
 'Rating'
 ],axis=1)

# Removing 'Unknown'
#English
new_ani['English']=np.where(new_ani['English']=='Unknown',new_ani['Title'],new_ani['English'])
#Others
new_ani=new_ani.replace("Unknown", "")

new_ani=new_ani.drop(['Title'],axis=1)

# synopsis alteration
ps = PorterStemmer()
def remove_splChar_normalizeWords(ss_line):
    word_list = []
    ss_line = re.sub('[^A-Za-z0-9]',' ', ss_line)
    #ss_line.replace('\n','')
    for word in ss_line.split():
        word_list.append(ps.stem(word))    
    return  " ".join(word_list)


new_ani['Modified Synopsis'] = new_ani['Synopsis'].apply(remove_splChar_normalizeWords)

#remove commas and creating new column
new_ani["Tags"] = new_ani['Modified Synopsis'] + " " + new_ani['Source'] + " " +[v.replace(',','') for v in new_ani['Producers']] + " " + [v.replace(',','') for v in new_ani['Studios']] + " " +[v.replace(',','') for v in new_ani['Genres']] + " " + [v.replace(',','') for v in new_ani['Themes']] + " " +[v.replace(',','') for v in new_ani['Demographics']]

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





