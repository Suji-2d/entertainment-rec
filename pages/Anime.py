import streamlit as st
import pandas as pd
import numpy as np
#import model.anime_model as am
from PIL import Image

anime_img = Image.open('./data/images/anime2.jpeg')


st.write("""
## Anime recommender
#### Kon'nichiwa! page is still under construction!!
""")
# st.write("""
# ## Anime recommender
# #### Kon'nichiwa! its time to watch anime!!
# """)

# titles = st.selectbox(
#     f'What is your favorite Anime',
#     am.getAllTitlesAvailable())

# st.write('You selected:', titles)

# def tableDisplay(tabList,col):
#     df = pd.DataFrame(
#     tabList,
#     columns=('Name',col))

#     hide_table_row_index = """
#         <style>
#         thead tr th:first-child {display:none}
#         tbody th {display:none}
#         </style>
#         """
#     # Inject CSS with Markdown
#     st.markdown(hide_table_row_index, unsafe_allow_html=True)

#     st.table(df)
# if st.button('Get recommendations'):
#     tableDisplay(am.give_rec(titles),'Rating')

# st.write("""
# ---
# """)
# st.image(anime_img, caption="Sayounara!!")
