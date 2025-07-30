import pandas as pd

# Load the dataset
df = pd.read_csv("spotify data/SpotifyAudioFeaturesApril2019.csv")

# Select only the features we care about
features = [
    'danceability', 'energy', 'loudness', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness',
    'valence', 'tempo', 'duration_ms', 'popularity'
]

df = df[features]

# Drop rows with missing values
df.dropna(inplace=True)

# Filter out extreme outliers in 'popularity'
df = df[df['popularity'] >= 0]

# Define a hit song as popularity >= 75
df['is_hit'] = df['popularity'] >= 75

# Print summary
print("✅ Cleaned dataset:")
print(df.head())
print("\nNumber of songs considered 'hits':", df['is_hit'].sum())
print("Total songs:", len(df))


