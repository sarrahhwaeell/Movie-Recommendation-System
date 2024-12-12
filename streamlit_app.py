import streamlit as st
import pickle
import urllib.request
import os

# Function to download and load .pkl files from URLs or local paths
@st.cache_resource
def load_pickle(file_url=None, file_name=None):
    if file_url:  # If a URL is provided, download the file
        if not os.path.exists(file_name):
            urllib.request.urlretrieve(file_url, file_name)
    if file_name:  # Load from a local file
        with open(file_name, 'rb') as file:
            return pickle.load(file)
    raise ValueError("Both file_url and file_name are missing!")

# Paths and URLs for your .pkl files
movie_list_url = "https://github.com/sarrahhwaeell/Movie-Recommendation-System/releases/download/v1.0.0-initial-release/movie_list.pkl"
movie_list_path = "movies_list.pkl"  # Local filename
similarity_matrix_url = "https://github.com/sarrahhwaeell/Movie-Recommendation-System/releases/download/v1.0.0-initial-release/similarity_matrix.pkl"
similarity_matrix_path = "similarity_matrix.pkl"

# Load .pkl files
movie_list = load_pickle(file_url=movie_list_url, file_name=movie_list_path)  # Download and load movies_list.pkl
similarity_matrix = load_pickle(file_url=similarity_matrix_url, file_name=similarity_matrix_path)  # Download and load similarity_matrix.pkl

# Streamlit app
st.title('Movie Recommendation System')

movie_name = st.text_input('Enter a Movie Name')

# Recommendation logic
def recommend(movie_name):
    try:
        movie_idx = movie_list[movie_list['title'] == movie_name].index[0]
        similarity_scores = list(enumerate(similarity_matrix[movie_idx]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

        recommended_movies = []
        for i in range(1, 6):
            movie_idx = similarity_scores[i][0]
            recommended_movies.append(movie_list['title'].iloc[movie_idx])

        return recommended_movies

    except Exception as e:
        return f"Error: {str(e)}"

if movie_name:
    recommendations = recommend(movie_name)
    st.write(f"Recommendations for '{movie_name}':")
    st.write(recommendations)
