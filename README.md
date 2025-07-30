# 🎧 HitSense: Predicting Song Popularity from Spotify Audio Features

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bedrock510/HitSense-Plus/blob/main/HitSense_EDA_and_Model_Full_FINAL.ipynb)

## 🔍 Project Overview

HitSense is a machine learning project that explores how audio features—such as energy, tempo, valence, and danceability—affect a song’s popularity on Spotify. The goal is to uncover predictive patterns and build a regression model to estimate popularity scores from track-level features.

This project was completed as part of a data science capstone, and is intended to demonstrate end-to-end data science workflow, from data preparation and visualization to modeling and evaluation.

---

## 🎯 Problem Statement

Can we predict a song’s popularity based on its audio attributes? This project seeks to answer that by applying machine learning to Spotify track-level data.

---

## 📁 Data Acquisition

The dataset is based on Spotify audio features, such as:
- Danceability
- Energy
- Tempo
- Valence
- Acousticness

For a full production version, data can be expanded via the Spotify Web API or third-party music analytics platforms to capture a larger and more diverse sample.

---

## 🧹 Data Preprocessing

- ✅ Checked for missing values (none present in sample data)
- ✅ Selected numeric features for modeling
- ✅ Used an 80/20 train-test split
- ✅ No categorical encoding needed (features are all numeric)

---

## 🤖 Modeling Approach

This project uses a **supervised learning approach** with a **Linear Regression** model to predict numerical song popularity.

Modeling Steps:
- Selected 5 input features (`danceability`, `energy`, `tempo`, `valence`, `acousticness`)
- Trained on 80% of the data
- Evaluated on 20% using standard metrics

---

## 📐 Model Evaluation

We evaluated the model using:
- **Mean Squared Error (MSE)**: to measure prediction error
- **R² Score**: to determine variance explained by the model

The baseline linear model showed moderate predictive power (R² ~ 0.60). Future enhancements may include:
- Feature engineering (e.g., genres, artist stats)
- Non-linear models (e.g., Random Forest, XGBoost)
- More training data

---

## 📈 Key Visualizations

- Distribution plots of each audio feature
- Heatmap showing correlations between features and popularity

---

## ✅ Results & Business Recommendations

- **Danceability** and **energy** have the strongest relationship with popularity.
- Suggests upbeat, high-energy songs tend to perform better.
- The model provides a foundation for building a hit prediction engine — useful for record labels, artists, and music marketers.

---

## 💻 How to Run

1. Open [`HitSense_EDA_and_Model_Full_FINAL.ipynb`](HitSense_EDA_and_Model_Full_FINAL.ipynb)
2. Run all cells in order (or launch in Colab using the badge above)
3. Optional: Train new models using `train_model.py`

---

## 🧾 .gitignore Recommendations

We've included a `.gitignore` file that excludes:
- Cache files (`__pycache__`, `.ipynb_checkpoints`)
- OS files (`.DS_Store`)
- Large files (`*.pkl`, `*.zip`)

---

## 👨‍💻 Author & Attribution

This project was developed as part of a capstone to demonstrate applied machine learning using real-world music data.

