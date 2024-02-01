# Movie Recommendation System Summary
## Overview
This movie recommendation system employs Natural Language Processing (NLP) techniques, specifically TF-IDF and content-based filtering, to provide personalized movie, series, and anime suggestions. By utilizing cosine similarity, the system offers top 10 recommendations based on the user's selected movie, series, or anime.

*Features*
- Content-Based Filtering: Recommends items based on their features, such as plot, genre, and keywords.

- TF-IDF (Term Frequency-Inverse Document Frequency): Extracts relevant features using NLP for a more nuanced understanding of content.

- Cosine Similarity: Measures the similarity between items, aiding in the generation of closely related recommendations.

Top 10 Recommendations: Provides a curated list of recommendations for an enhanced viewing experience.

## Deployment
The system is deployed using Streamlit, making it accessible through a user-friendly web interface. Users can run the application locally by following the provided steps and enjoy personalized recommendations.

## Usage
Select a movie, series, or anime from the provided list.

Click "Get Recommendations."

Explore the top 10 recommendations based on your selection.

Note
This implementation serves as a foundational recommendation system. Users are encouraged to customize the code and dataset for improved accuracy and relevance. Happy watching! 🍿

Deployment platform: Stremlit  
App-link: https://suji-2d-entertainment-rec-home-j85wxs.streamlit.app/  (APP may take little time to load)

BUG: In movies data set 'Scream', 'Spider-Man' movie name have duplicate issue - remove duplicare enteries in all data set
