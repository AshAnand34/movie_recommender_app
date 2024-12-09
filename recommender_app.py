import streamlit as st, numpy as np, pandas as pd

# Make the web app wide-screen
st.set_page_config(layout="wide")

from IBCF import load_movies, parse_movie_img, myIBCF

st.title("Movie Recommender System")

st.header("Rate your favorite movies!")

# Loads the all the movies and selects 100 of them to be rated by the users
all_movies = load_movies()

displayed_movies = all_movies.head(100)

# Store user ratings
user_ratings = {}

for i in range(10):
    cols = st.columns(10)

    for j in range(10):
        movie = displayed_movies.iloc[10*i + j, :]
        cols[j].image(parse_movie_img(movie["movie_id"]), caption=movie["title"], use_container_width=True)
        rating = cols[j].feedback("stars", key=movie["movie_id"])
        if rating is not None: # Store rating if the user has given one
            user_ratings[movie["movie_id"]] = rating

if st.button("Submit"):
    #st.write("I am the next biggest star of Hollywood!!")
    if not user_ratings:
        st.write("No ratings provided! Please rate some movies.")
    else:
        # Convert user ratings to Series
        new_user = pd.Series(user_ratings)

        # Generate recommendations
        recommendations = myIBCF(new_user, top_n=10)

        # Display top 10 recommended movies
        st.header("Top 10 Recommended Movies for You!")
        cols = st.columns(10)
        for i in range(min(10, len(recommendations))): # Ensure no out of bounds errors
            movie_id = recommendations.iloc[i]['movie_id']
            movie_title = all_movies.loc[all_movies['movie_id'] == movie_id, 'title'].values[0]
            cols[i].image(parse_movie_img(movie_id), caption=movie_title, use_container_width=True)


#st.header("Here are the top 10 movies for you to check out next")

# TODO: Replace this with actual implementation of 
# 2) Use the ratings provided by the user as input for your myIBCF function.
#top_10_movies = all_movies.sample(n=10)
#cols = st.columns(10)
#for i in range(10):
    #movie = top_10_movies.iloc[i]
    #cols[i].image(parse_movie_img(movie["movie_id"]), caption=movie["title"], use_container_width=True)
