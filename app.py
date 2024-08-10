import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=be8e906ce1a0b7081cf67c64c2ebc6d8&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']

def recommend(movies):
    index = movie[movie['original_title'] == movies].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recomended_movies=[]
    recommend_movies_poster=[]
    for i in distances[1:6]:
        movies_id=movie.iloc[i[0]].id


        recomended_movies.append(movie.iloc[i[0]].original_title)
        recommend_movies_poster.append(fetch_poster(movies_id))
    return recomended_movies,recommend_movies_poster

movie_dict=pickle.load(open('movie_dict.pkl', 'rb'))
movie=pd.DataFrame(movie_dict)

similarity=pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movie['original_title'].values,
)


if st.button("Recommend"):
    names,posters = recommend(selected_movie_name)


    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])


