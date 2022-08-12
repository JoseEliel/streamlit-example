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

posts = []
with open('posts.csv', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentpost = line[:-1]
        # add item to the list
        posts.append(currentpost)

st.title('Las Nubes de Palabras de Paul')

form = st.form(key='my-form')
post = form.text_input('Escriba su texto bonito')
submit = form.form_submit_button('Enviar')

if submit:
    posts.append(post)
    
    with open('posts.csv', 'w') as filehandle:
    for listitem in posts:
        filehandle.write('%s\n' % listitem)
        
    unique_string=(" ").join(''.join(l) for l in posts)
    wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
    fig = plt.figure(figsize=(15,8))
    plt.imshow(wordcloud)
    plt.axis("off")

    plt.show()
    st.pyplot(fig)

with open('posts.csv', 'r') as myfile:
    st.download_button('Bajar posts', myfile, file_name='posts.csv')

with st.container():
    st.header("Post antiguos")
    for post in posts:
        st.text(post)
        

