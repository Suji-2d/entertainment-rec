import streamlit as st
import pandas as pd
import numpy as np
import model.tvseries_model as tm
from PIL import Image

series_img = Image.open('./data/images/series3.jpeg')

st.write("""
## Series recommender
#### Welcome! its time to watch series!!
""")

titles = st.selectbox(
    f'What is your favorite Series',
    tm.getAllTitlesAvailable())

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
    tableDisplay(tm.give_rec(titles),'Rating')

st.write("""
---
""")
st.image(series_img, caption="see you next time!!")