import pandas as pd
import numpy as np
import re
import random
from nltk.stem.porter import PorterStemmer
from pathlib import Path  
anime_path = Path('./data/clean_data/anime.csv')  
anime_path.parent.mkdir(parents=True, exist_ok=True)  


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

new_ani.to_csv(anime_path)