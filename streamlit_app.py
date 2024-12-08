import streamlit as st
import pickle
import urllib.request
import os
import requests

# Function to download a file from Google Drive
def download_from_google_drive(file_id, destination):
    base_url = "https://drive.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(base_url, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)
    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(base_url, params=params, stream=True)
    save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination):
    chunk_size = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(chunk_size):
            if chunk:
                f.write(chunk)

# File paths and URLs
movie_list_url = "https://raw.githubusercontent.com/sarrahhwaeell/Movie-Recommendation-System/main/movie_list.pkl"
movie_list_path = "movie_list.pkl"
similarity_matrix_path = "similarity_matrix.pkl"

# Google Drive file ID for similarity_matrix.pkl
similarity_matrix_file_id = "14d1ajYL7uOI_YBc2zQLRMLRU2mDCn4kU"

# Function to load .pkl files
@st.cache_resource
def load_pickle(file_path, url=None, google_drive_id=None):
    if not os.path.exists(file_path):
        if google_drive_id:
            download_from_google_drive(google_drive_id, file_path)
        elif url:
            urllib.request.urlretrieve(url, file_path)
    with open(file_path, 'rb') as file:
        return pickle.load(file)

# Load the .pkl files
movie_list = load_pickle(movie_list_path, url=movie_list_url)
similarity_matrix = load_pickle(similarity_matrix_path, google_drive_id=similarity_matrix_file_id)

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
