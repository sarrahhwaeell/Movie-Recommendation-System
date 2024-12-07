import streamlit as st
import pickle
import pandas as pd

# Load the pre-trained models
with open('movie_list.pkl', 'rb') as f:
    movie_list = pickle.load(f)

with open('similarity_matrix.pkl', 'rb') as f:
    similarity_matrix = pickle.load(f)

# Set the title for your Streamlit app
st.title('Movie Recommendation System')

# Create an input text box for the user to enter the movie name
movie_name = st.text_input('Enter a Movie Name')

# Function to get movie recommendations
def recommend(movie_name):
    try:
        # Find movie index and make recommendations
        movie_idx = movie_list[movie_list['title'] == movie_name].index[0]
        similarity_scores = list(enumerate(similarity_matrix[movie_idx]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        
        # Get top 5 recommended movies
        recommended_movies = []
        for i in range(1, 6):
            movie_idx = similarity_scores[i][0]
            recommended_movies.append(movie_list['title'].iloc[movie_idx])
        
        return recommended_movies
    
    except Exception as e:
        return f"Error: {str(e)}"

# When the user clicks the button to get recommendations
if movie_name:
    recommendations = recommend(movie_name)
    st.write(f"Recommendations for '{movie_name}':")
    st.write(recommendations)


