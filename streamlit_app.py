import streamlit as st
import pickle

# Set the paths to the downloaded .pkl files
movie_list_path = 'path_to_your_local_drive/Movie recommendation system/movie_list.pkl'
similarity_matrix_path = 'path_to_your_local_drive/Movie recommendation system/similarity_matrix.pkl'

# Load the .pkl files
with open(movie_list_path, 'rb') as f:
    movie_list = pickle.load(f)

with open(similarity_matrix_path, 'rb') as f:
    similarity_matrix = pickle.load(f)

# Display Streamlit app content
st.title('Movie Recommendation System')

movie_name = st.text_input('Enter a Movie Name')

# Recommendation logic remains the same
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
