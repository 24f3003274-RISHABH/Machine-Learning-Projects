

import streamlit as st
import pickle

import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da8d42e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

    
    

def recommend(movie):
    index = movie_list[movie_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []

    for i in distances[1:6]:
        recommended_movie_names.append(movie_list.iloc[i[0]].title)
    return recommended_movie_names

similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_list = pickle.load(open('movie_list.pkl', 'rb'))   # keep as DataFrame

st.title("Movie Recommender System")
st.title("Welcome to the Movie Recommender System!")

option = st.selectbox(
    'Select your favorite movie:',
    movie_list['title'].values   # only here use .values for dropdown
)

if st.button('Recommend'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)

