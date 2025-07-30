from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import uvicorn

# Load the trained model
model = joblib.load("hitsense_model.pkl")

# Create the app
app = FastAPI(title="HitSense API")

# Define the input data structure
class SongFeatures(BaseModel):
    danceability: float
    energy: float
    loudness: float
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    duration_ms: int

# Define some simulated hit averages for comparison
avg_features = {
    "tempo": 110,
    "energy": 0.75,
    "danceability": 0.72,
    "valence": 0.65,
}

# Prediction endpoint
@app.post("/predict")
def predict_hit_potential(features: SongFeatures):
    try:
        df = pd.DataFrame([features.dict()])
        prob = model.predict_proba(df)[0][1]
        hit_score = round(prob * 100, 2)

        # Generate a simple report card
        report = {}
        for key in avg_features:
            value = getattr(features, key)
            avg = avg_features[key]
            status = "good" if abs(value - avg) < 0.1 * avg else "off"
            report[key] = {"value": value, "avg": avg, "status": status}

        status = (
            "high" if hit_score > 60 else
            "medium" if hit_score > 40 else
            "low"
        )

        return {
            "hit_score": hit_score,
            "prediction_status": status,
            "feature_analysis": report
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Optional: Run locally for testing
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

