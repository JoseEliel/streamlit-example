from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import csv
from pathlib import Path
from wordcloud import WordCloud
import matplotlib.pyplot as plt


fle = Path('posts.csv')
fle.touch(exist_ok=True)
"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
with open('posts.csv', newline='') as f:
    reader = csv.reader(f)
    posts = list(reader)

st.title('Las Nubes de Palabras de Paul')

form = st.form(key='my-form')
post = form.text_input('Escriba su texto bonito')
submit = form.form_submit_button('Enviar')

if submit:
    posts.append(post)
    
    with open('posts.csv', 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(posts)
        
    unique_string=(" ").join(''.join(l) for l in posts)
    wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
    fig = plt.figure(figsize=(15,8))
    plt.imshow(wordcloud)
    plt.axis("off")

    plt.show()
    st.pyplot(fig)
    
