import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

# Drop and recreate the movies table (Only if you need a fresh start)
cursor.execute("DROP TABLE IF EXISTS movies;")
cursor.execute("""
CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    genre TEXT,
    overview TEXT,
    vote_average REAL
);
""")

# Load cleaned dataset
df = pd.read_csv("movies_cleaned.csv")

# Insert data into SQLite
for _, row in df.iterrows():
    cursor.execute("INSERT INTO movies (title, genre, overview, vote_average) VALUES (?, ?, ?, ?)", 
                   (row["title"], row["genres"], row["overview"], row["vote_average"]))

# Commit changes and close the connection
conn.commit()
conn.close()

print("✅ Full cleaned movie dataset (with overviews) imported into movies.db!")
