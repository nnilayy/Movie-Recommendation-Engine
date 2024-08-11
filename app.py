import pickle
import streamlit as st
import requests
import pandas as pd
import os

# # -----------------------------------------------------------------------------
# #-----------------------------------------------------------------------------
# # IF WORKING LOCALLY, USE dotenv TO LOAD THE API KEY
# from dotenv import load_dotenv 
# load_dotenv()
# tmdb_api_key = os.getenv('TMDB_API_KEY')
# #-----------------------------------------------------------------------------
# #-----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# USING STREAMLIT SECRETS TO LOAD THE API KEY FOR DEPLOYMENT
tmdb_api_key = st.secrets["TMDB_API_KEY"]
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def fetch_poster(movie_id):
    print(movie_id)
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_key}&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['titles'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].titles)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movie_dict = pickle.load(open('model_files/movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('model_files/similarity.pkl','rb'))

movie_list = movies['titles'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)  # Updated from st.beta_columns to st.columns
    for i, col in enumerate(cols):
        with col:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])
