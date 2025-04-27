import pandas as pd
import json

# Load the dataset
df = pd.read_csv("movies_metadata.csv")

# Drop unnecessary columns (modify based on actual dataset)
df = df[["title", "genres", "overview", "vote_average"]]

# Function to clean genres
def clean_genres(genre_data):
    try:
        genre_list = json.loads(genre_data.replace("'", '"'))  # Convert JSON-like format
        return ", ".join([genre["name"] for genre in genre_list])  # Extract genre names
    except:
        return ""  # Return empty if there's an error

# Apply genre cleaning function
df["genres"] = df["genres"].apply(clean_genres)

# Convert rating to float & remove invalid values
df["vote_average"] = pd.to_numeric(df["vote_average"], errors="coerce")
df = df.dropna(subset=["vote_average"])  # Remove rows where rating is NaN

# Remove duplicates
df = df.drop_duplicates()

# Save the cleaned dataset
df.to_csv("movies_cleaned.csv", index=False)

print("✅ Data cleaned and saved as 'movies_cleaned.csv'!")