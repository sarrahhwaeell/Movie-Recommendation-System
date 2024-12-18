# Movie Recommendation System

This project implements a **Movie Recommendation System** that suggests movies to users based on their preferences using various recommendation algorithms such as **Collaborative Filtering**, **Content-Based Filtering**, and **Hybrid Recommender Systems**. It leverages machine learning techniques and a movie dataset to provide personalized movie recommendations.

## Data source 
The TMDB 5000 Movie Dataset from kaggle https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata 


## Project Description

This **Movie Recommendation System** allows users to receive personalized movie suggestions based on their viewing history or similar user preferences. The system can use **Collaborative Filtering**, which recommends movies based on the ratings and preferences of similar users, and **Content-Based Filtering**, which recommends movies based on the features (e.g., genre, director) of the movies that a user has liked.

### Features:
- Personalized movie recommendations based on user input.
- Collaborative filtering for user-item interactions.
- Content-based recommendations based on movie metadata.
- Hybrid recommender system combining both approaches for more accurate results.

## Technologies Used

- **Python** (for data processing, machine learning models)
- **pandas** (data manipulation)
- **scikit-learn** (machine learning algorithms)
- **numpy** (numerical operations)
- **matplotlib & seaborn** (visualization)
- **Streamlit** (for web application interface)
- **Cosine Similarity**: Developed a movie recommendation system using cosine similarity, a method for measuring the similarity between two vectors of an inner product space. Cosine similarity is used here to recommend movies based on user preferences and movie features.
- **Natural Language Processing (NLP)**: Applied NLP techniques for text processing to convert movie metadata such as movie descriptions into numerical features.
- **TF-IDF (Term Frequency-Inverse Document Frequency)**: Implemented vectorization techniques such as TF-IDF to convert text data into numerical features, improving the recommendation accuracy by capturing the importance of terms in movie descriptions.





