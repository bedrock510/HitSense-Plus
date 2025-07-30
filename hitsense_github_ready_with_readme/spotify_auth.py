print("✅ Running Spotify Auth via User Login")

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="b588527e0cfb434e967595b473886975",
    client_secret="cf70b0b6942c444fa79b24fb035da097",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-library-read"
))

# Use Spotify search to get track ID
results = sp.search(q="Blinding Lights The Weeknd", type="track", limit=1)
track_id = results['tracks']['items'][0]['id']

# Pull audio features
features = sp.audio_features([track_id])[0]

# Show results
print("🎵 Track Features:")
print(f"Tempo (BPM): {features['tempo']}")
print(f"Key: {features['key']}")
print(f"Danceability: {features['danceability']}")
print(f"Energy: {features['energy']}")
print(f"Valence (Mood): {features['valence']}")
