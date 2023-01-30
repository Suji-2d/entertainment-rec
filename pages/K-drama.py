import streamlit as st
import pandas as pd
import numpy as np
import model.kdrama_model as km
from PIL import Image

kdrama_img = Image.open('./data/images/kdrama2.png')

st.write("""
## K-drama recommender
#### Annyeonghaseyo! its time to watch K-drama!!
""")

titles = st.selectbox(
    f'What is your favorite K-drama',
    km.getAllTitlesAvailable())

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
    tableDisplay(km.give_rec(titles),'Rating')

st.write("""
---
""")
st.image(kdrama_img, caption="annyeong!!")