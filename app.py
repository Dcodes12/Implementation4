from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random  # Needed for shuffling

app = Flask(__name__)
CORS(app)

def get_db_connection():
    """Connect to SQLite database."""
    conn = sqlite3.connect("movies.db")
    conn.row_factory = sqlite3.Row
    return conn

# Function to get movie data
def fetch_movies():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT title, genre, overview, vote_average FROM movies")
    
    # Convert SQLite rows to a list of dictionaries
    movies = [dict(row) for row in cursor.fetchall()]
    conn.close()
    
    return pd.DataFrame(movies)

# Function to process user input and find similar movies
def recommend_movies(user_input):
    movies_df = fetch_movies()

    if movies_df.empty:
        return []

    # Fill missing overviews
    movies_df["overview"] = movies_df["overview"].fillna("")

    # Vectorize movie overviews
    tfidf_vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df["overview"])

    # Transform user input
    user_tfidf = tfidf_vectorizer.transform([user_input])

    # Calculate similarity scores
    similarities = cosine_similarity(user_tfidf, tfidf_matrix).flatten()

    # Get top 50 instead of 20
    top_indices = similarities.argsort()[-50:][::-1]
    random.shuffle(top_indices)
    top_indices = top_indices[:6]


    recommendations = []
    for i in top_indices:
        recommendations.append({
            "title": movies_df.iloc[i]["title"],
            "genre": movies_df.iloc[i]["genre"],
            "overview": movies_df.iloc[i]["overview"],
            "vote_average": movies_df.iloc[i]["vote_average"]
        })

    return recommendations

@app.route("/search", methods=["POST"])
def search_movies():
    """API endpoint to search movies based on user input."""
    data = request.json
    user_input = data.get("query", "")

    if not user_input:
        return jsonify({"error": "No query provided"}), 400

    recommendations = recommend_movies(user_input)
    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
