import streamlit as st, numpy as np, pandas as pd

# Make the web app wide-screen
st.set_page_config(layout="wide")

from IBCF import load_movies, parse_movie_img, myIBCF

st.title("Movie Recommender System")

# Loads the all the movies and selects 100 of them to be rated by the users
all_movies = load_movies()

displayed_movies = all_movies.head(100)

for i in range(10):
    cols = st.columns(10)

    for j in range(10):
        movie = displayed_movies.iloc[10*i + j, :]
        cols[j].image(parse_movie_img(movie["movie_id"]), caption=movie["title"], use_container_width=True)
        cols[j].feedback("stars", key=movie["movie_id"])

if st.button("Submit"):
    st.write("I am the next biggest star of Hollywood!!")