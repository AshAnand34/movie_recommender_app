import pandas as pd

def load_top_ten_movies():
    top_ten_movies = pd.read_csv("data/top_10_popular_movies.csv")
    top_ten_movies['movie_img'] = top_ten_movies['movie_img'] + '.jpg?raw=true'
    return top_ten_movies