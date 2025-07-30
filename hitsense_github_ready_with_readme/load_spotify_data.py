import pandas as pd

# Load the dataset
df = pd.read_csv("spotify data/SpotifyAudioFeaturesApril2019.csv")

# Show basic info
print("✅ Dataset loaded successfully!")
print(df.shape)
print(df.columns)
print(df.head(3))


import pandas as pd

# Load the dataset
df = pd.read_csv("spotify data/SpotifyAudioFeaturesApril2019.csv")

# Show basic info
print("✅ Dataset loaded successfully!")
print(df.shape)
print(df.columns)
print(df.head(3))

import pandas as pd

# Load the dataset
df = pd.read_csv("spotify data/SpotifyAudioFeaturesApril2019.csv")

# Show basic info
print("✅ Dataset loaded successfully!")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Preview:")
print(df.head(3))

