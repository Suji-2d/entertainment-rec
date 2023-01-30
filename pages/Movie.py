import streamlit as st
import pandas as pd
import numpy as np
import model.movie_model as mm
from PIL import Image

movie_img = Image.open('./data/images/movies1.jpeg')

st.write("""
## Movie recommender
#### Welcom! its time to watch movie!!
""")

titles = st.selectbox(
    f'What is your favorite Movie',
    mm.getAllTitlesAvailable())

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
    tableDisplay(mm.give_rec(titles),'Rating')

st.write("""
---
""")
st.image(movie_img, caption="see you next time!!")