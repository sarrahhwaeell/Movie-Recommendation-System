import streamlit as st
import pickle
import urllib.request
import os
import requests

# Function to download and load .pkl files from URLs or local paths
@st.cache_resource
def load_pickle(file_url, file_name):
    if not os.path.exists(file_name):
        urllib.request.urlretrieve(file_url, file_name)
    with open(file_name, 'rb') as file:
        return pickle.load(file)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data.get('poster_path', '')
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# URLs for your .pkl files
movie_list_path = "movies_list.pkl"  # This is directly in your GitHub repo
similarity_matrix_url = "https://github.com/sarrahhwaeell/Movie-Recommendation-System/releases/download/v1.0.0-initial-release/similarity_matrix.pkl"
similarity_matrix_path = "similarity_matrix.pkl"

# Load .pkl files
movie_list = load_pickle(movie_list_path, movie_list_path)
similarity_matrix = load_pickle(similarity_matrix_url, similarity_matrix_path)

# Streamlit app
st.header('Movie Recommendation System')

movie_titles = movie_list['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_titles
)

# Recommendation logic
def recommend(movie_name):
    try:
        movie_idx = movie_list[movie_list['title'] == movie_name].index[0]
        similarity_scores = list(enumerate(similarity_matrix[movie_idx]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

        recommended_movie_names = []
        recommended_movie_posters = []
        for i in similarity_scores[1:6]:
            recommended_movie_names.append(movie_list['title'].iloc[i[0]])
            # Placeholder for poster fetching logic (assuming movie_id is part of the dataset)
            movie_id = movie_list.iloc[i[0]].get('movie_id', None)
            if movie_id:
                recommended_movie_posters.append(fetch_poster(movie_id))
            else:
                recommended_movie_posters.append("https://via.placeholder.com/150")  # Default poster

        return recommended_movie_names, recommended_movie_posters

    except Exception as e:
        return [f"Error: {str(e)}"], ["https://via.placeholder.com/150"] * 5

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
