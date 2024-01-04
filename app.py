import streamlit as st #to genrate user interface
import pickle#to import the pickles file
import pandas as pd #to access the tabular data
import requests#to request to browser to open the url

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8ae1e5cb3b522ec7ae2bc1394580ee56&language=en-US'.format(movie_id))

    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # find the index of movie
    distances = distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])


    recommended_movies = []
    recommended_movies_poster = []
    for i in distances[1:6]:

        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

##########################################################
movies_dict= pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title("MOVIE RECOMENDER SYSTEM")

movie_list = movies['title'].values
selected_movies = st.selectbox(
    "Type or select a movie from the dropdown",
   movie_list
)

if st.button('Recommend'):
    recommended_movie,recommended_movie_posters=recommend(selected_movies)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie[4])
        st.image(recommended_movie_posters[4])





