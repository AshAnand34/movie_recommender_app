import streamlit as st, numpy as np, pandas as pd

# Make the web app wide-screen
st.set_page_config(layout="wide")

from IBCF import load_movies, parse_movie_img, myIBCF
# TODO: Clean up this import if unused after the TODO for 
# step 2 below is completed.
from IBCF import load_top_ten_movies

st.title("Movie Recommender System")

st.header("Rate your favorite movies!")

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

st.header("Here are the top 10 movies for you to check out next")

# TODO: Replace this with actual implementation of 
# 2) Use the ratings provided by the user as input for your myIBCF function.
top_10_movies = all_movies.sample(n=10)
cols = st.columns(10)
for i in range(10):
    movie = top_10_movies.iloc[i]
    cols[i].image(parse_movie_img(movie["movie_id"]), caption=movie["title"], use_container_width=True)


