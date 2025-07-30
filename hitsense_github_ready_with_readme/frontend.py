import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import tempfile
import os

st.set_page_config(page_title="HitSense", layout="wide")

# Neon UI with black background
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
        background-color: #000000;
        color: white;
    }
    .block-container {
        padding: 2rem 4rem;
    }
    .section-card {
        background: #111111;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.08);
        border: 1px solid rgba(0,255,255,0.05);
        margin-bottom: 2rem;
    }
    .section-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        color: #4de3ff;
    }
    .stButton>button {
        background-color: #1e90ff;
        color: white;
        border: none;
        padding: 0.6rem 1.4rem;
        border-radius: 8px;
        font-weight: 600;
        box-shadow: 0 0 8px rgba(30,144,255,0.6);
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #00bfff;
        box-shadow: 0 0 12px rgba(0,191,255,0.9);
    }
    input, .stTextInput>div>div>input {
        background-color: #1e1f25;
        border: 1px solid #4de3ff;
        color: white;
        border-radius: 8px;
        padding: 0.6rem;
    }
    .stSlider>div>div>div {
        background-color: #4de3ff !important;
    }
    .stSlider>div>div>div>div {
        background-color: #00bfff !important;
    }
    </style>
""", unsafe_allow_html=True)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

st.markdown("<h1 style='color:#4de3ff;'>🎧 HitSense Dashboard</h1>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🎵 Upload/Spotify", "📈 Results"])
autofill_features = {}

with tab1:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Spotify Autofill</div>', unsafe_allow_html=True)
    spotify_link = st.text_input("Paste Spotify Track URL or ID:")
    if st.button("Autofill from Spotify"):
        try:
            track_id = spotify_link.strip().split("/")[-1].split("?")[0]
            features = sp.audio_features([track_id])[0]
            autofill_features = features if features else {}
            st.success("Track features loaded.")
        except Exception as e:
            st.error(f"Error: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Upload WAV or MP3</div>', unsafe_allow_html=True)
    uploaded_audio = st.file_uploader("Upload audio file", type=["wav", "mp3"])
    if uploaded_audio:
        with tempfile.NamedTemporaryFile(delete=False, suffix="." + uploaded_audio.name.split(".")[-1]) as tmp:
            tmp.write(uploaded_audio.read())
            tmp_path = tmp.name
        try:
            y, sr = librosa.load(tmp_path, sr=None)
            tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
            rms = np.mean(librosa.feature.rms(y=y))
            loudness = 20 * np.log10(rms + 1e-6)
            duration_ms = int(librosa.get_duration(y=y, sr=sr) * 1000)

            autofill_features.update({
                "tempo": tempo,
                "energy": float(min(max(rms * 10, 0), 1)),
                "loudness": float(loudness),
                "duration_ms": duration_ms,
            })

            st.success("Audio features extracted.")
            fig, ax = plt.subplots(figsize=(6, 2))
            librosa.display.waveshow(y, sr=sr, alpha=0.7, ax=ax)
            ax.set_title("Waveform")
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Audio processing failed: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Adjust Features</div>', unsafe_allow_html=True)
    with st.form("feature_form"):
        tempo = st.slider("Tempo", 50, 200, int(autofill_features.get("tempo", 120)))
        energy = st.slider("Energy", 0.0, 1.0, float(autofill_features.get("energy", 0.7)))
        danceability = st.slider("Danceability", 0.0, 1.0, float(autofill_features.get("danceability", 0.68)))
        valence = st.slider("Valence", 0.0, 1.0, float(autofill_features.get("valence", 0.3)))
        speechiness = st.slider("Speechiness", 0.0, 1.0, float(autofill_features.get("speechiness", 0.5)))
        loudness = float(autofill_features.get("loudness", -10.0))
        duration_ms = int(autofill_features.get("duration_ms", 180000))
        submitted = st.form_submit_button("Run Prediction")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    if submitted:
        data = {
            "danceability": danceability,
            "energy": energy,
            "loudness": loudness,
            "speechiness": speechiness,
            "acousticness": 0.3,
            "instrumentalness": 0.0,
            "liveness": 0.2,
            "valence": valence,
            "tempo": tempo,
            "duration_ms": duration_ms
        }

        response = requests.post("http://127.0.0.1:8000/predict", json=data)

        if response.status_code == 200:
            result = response.json()
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">Prediction</div>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            col1.metric("Hit Score", f"{result['hit_score']}%")
            col2.metric("Prediction", result["prediction_status"].capitalize())
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">Feature Comparison</div>', unsafe_allow_html=True)
            df = pd.DataFrame(result["feature_analysis"]).T.rename(columns={"value": "Your Song", "avg": "Top 100 Avg"})
            st.dataframe(df)

            fig = go.Figure()
            fig.add_trace(go.Bar(x=df.index, y=df["Your Song"], name="Your Song", marker_color="#1e90ff"))
            fig.add_trace(go.Bar(x=df.index, y=df["Top 100 Avg"], name="Top 100 Avg", marker_color="#4de3ff"))
            fig.update_layout(barmode='group', height=400, title="Audio Feature Comparison",
                              paper_bgcolor='#000000', plot_bgcolor='#000000', font_color='white')
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error("API connection failed.")

