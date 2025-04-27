# Find4You - Movie and TV Show Recommendation System

## Overview
Find4You is a web-based application designed to help users quickly find personalised movie and TV show recommendations based on their preferences.  
Users can enter a free-text description of what they feel like watching, and the system returns six dynamic recommendations.

The project uses Natural Language Processing (NLP) techniques, including TF-IDF vectorisation and cosine similarity, to match user input against a curated movie database.

---

## Technologies Used
- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Libraries:** scikit-learn (for TF-IDF and cosine similarity)

---

## Features
- Natural language query processing
- Star rating system (out of six stars, including half-stars ✰)
- Hover-to-reveal movie descriptions
- Fade-in animations for improved UX
- Responsive design (desktop and mobile compatible)

---

## How to Run the Project

1. Clone this repository:

```bash
git clone https://github.com/Dcodes12/Implementation4

Navigate into the project directory:

bash
cd Implementation4
Ensure you have Flask installed. If not, install it:

bash 
pip install Flask
Run the Flask server:

bash
python app.py
Open index.html in a web browser to start using the application.
