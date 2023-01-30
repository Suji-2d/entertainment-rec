import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import model.kdrama_model as km
#import model.anime_model as am
import model.movie_model as mm
#import model.tvseries_model as tm

main_img = Image.open('./data/images/movie3.jpg')

st.write("""
# Enternainment recommender
#### Having struggle choosing what to watch next !?

Select the type of entertainment from the side-bar
""")


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

st.write("""
#### Quick suggestions!!
""")
randList=[]
randList.append([', '.join(mm.getRandomSuggestion(2)),'Movie'])
#randList.append([', '.join(tm.getRandomSuggestion(2)),'Series'])
randList.append([', '.join(km.getRandomSuggestion(2)),'K-drama'])
#randList.append([', '.join(am.getRandomSuggestion(2)),'Anime'])
tableDisplay(randList,'Type')

st.image(main_img)
