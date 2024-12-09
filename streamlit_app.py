import streamlit as st
import pickle
import urllib.request
import os

# Function to download and load .pkl files from URLs or local paths
@st.cache_resource
def load_pickle(file_url, file_name):
    if not os.path.exists(file_name):
        urllib.request.urlretrieve(file_url, file_name)
    with open(file_name, 'rb') as file:
        return pickle.load(file)

# Google Drive File ID for the similarity_matrix.pkl file
similarity_matrix_file_id = "14d1ajYL7uOI_YBc2zQLRMLRU2mDCn4kU"  # Replace with your actual file ID
similarity_matrix_url = f"https://drive.google.com/uc?export=download&id={similarity_matrix_file_id}"

# URLs for your .pkl files hosted online (replace with your actual URLs)
movie_list_url = "https://github.com/sarrahhwaeell/Movie-Recommendation-System/raw/main/movie_list.pkl"  # GitHub URL for movie_list.pkl

# Local file names to store the downloaded .pkl files
movie_list_path = "movie_list.pkl"
similarity_matrix_path = "similarity_matrix.pkl"

# Load .pkl files
movie_list = load_pickle(movie_list_url, movie_list_path)
similarity_matrix = load_pickle(similarity_matrix_url, similarity_matrix_path)

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
