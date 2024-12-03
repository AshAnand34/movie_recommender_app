import streamlit as st
from streamlit_carousel import carousel
from recommend_funs import load_top_ten_movies

# Make the web app wide-screen
st.set_page_config(layout="wide")

st.title("Movie Recommender App")

# Set up tabs for each recommender system
tab1, tab2 = st.tabs(["Top 10 Popular Movies", "Movie Recommending System"])

# First tab highlights the top 10 popular movies by average rating
top_ten_movies = load_top_ten_movies()

# Set up image data list for carousel to render
carousel_img_items = [
    dict(
        title=movie["title"],
        text=f"Avg Rating: {movie['avg_rating']:.2f}",
        img=movie["movie_img"],
    ) 
    for _, movie in top_ten_movies.iterrows()
]

tab1.text("Here are the top 10 popular movies based on the average ratings. Popularity in this case refers to having more than 1000 ratings for a movie.")

with tab1:
    carousel(items=carousel_img_items, container_height=350, width=0.18)

# Second tab implements the IBCF system such that it outputs top 10 recommended movies based on user ratings
tab2.image(top_ten_movies.iloc[2, 2], caption=top_ten_movies.iloc[2, 1])

selected_rating = tab2.feedback("stars")

if selected_rating is not None:
    st.markdown(f"{top_ten_movies.iloc[2, 1]} was rated {selected_rating + 1} stars")