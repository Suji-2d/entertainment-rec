import streamlit as st
import pandas as pd
import numpy as np
import model.kdrama_model as km
import model.anime_model as am
import model.tvseries_model as tm
import model.movie_model as mm


st.write("""
# Enternainment recommender
Struggle choosing what to watch next !?
""")
entList=["Anime","K-drama","Movie","Series"]
entr = st.radio("Select the type of entertainment",
        entList,
        horizontal=True,
        label_visibility='visible',
)
if(entr=='Anime'):
    gm=am
elif(entr=='Series') :
    gm =tm
elif(entr=='Movie') :
    gm =mm
else:
    gm=km

titles = st.selectbox(
    f'What is your favorite **{entr}**',
    gm.getAllTitlesAvailable())

st.write('You selected:', titles)

def tableDisplay(tabList,col):
    df = pd.DataFrame(
    tabList,
    columns=('Name',col))

    hide_table_row_index = """
        <style>
        thead tr th:first-child {display:none}
        tbody th {display:none}
        </style>
        """
    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    st.table(df)
if st.button('Get recommendations'):
    tableDisplay(gm.give_rec(titles),'Rating')
else:
    st.write("""
    #### Not sure what to choose!? then go with the universe's choice!
    """)
    randList=[]
    randList.append([', '.join(mm.getRandomSuggestion(2)),'Movie'])
    randList.append([', '.join(tm.getRandomSuggestion(2)),'Series'])
    randList.append([', '.join(km.getRandomSuggestion(2)),'K-drama'])
    randList.append([', '.join(am.getRandomSuggestion(2)),'Anime'])
    tableDisplay(randList,'Type')
