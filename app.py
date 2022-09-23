import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    responce =requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3da8a4e22cfd66fd3112fabb27eb983f&language=en-US'.format(movie_id))
    data=responce.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters =[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies =pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('movie recommender system')

selected_movie_name = st.selectbox(
    'how will you',
    movies['title'].values)

if st.button('recommend'):
    names,posters = recommend(selected_movie_name)
    cal1,cal2,cal3,cal4,cal5= st.beta_columns(5)
    with cal1:
        st.text(names[0])
        st.image(posters[0])
    with cal2:
        st.text(names[1])
        st.image(posters[1])
    with cal3:
        st.text(names[2])
        st.image(posters[2])
    with cal4:
        st.text(names[3])
        st.image(posters[3])
    with cal5:
        st.text(names[4])
        st.image(posters[4])
