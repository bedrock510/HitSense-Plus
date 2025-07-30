# 🎧 HitSense: Predicting Song Popularity on Spotify

## 🔍 Project Overview
HitSense explores how musical features like danceability, energy, tempo, and valence correlate with song popularity on Spotify. We use data-driven insights and machine learning models to predict popularity scores and guide music-related decisions.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/HitSense_EDA_and_Model_Full_FINAL.ipynb)

## 📁 Files
- `HitSense_EDA_and_Model_FULL_FINAL_WITH_CODE.ipynb`: Final notebook with all models, plots, evaluations, and commentary.
- `spotify data/`: Raw and processed feature data.
- `hitsense_model.pkl`: Trained model (Random Forest baseline).
- `model_comparison_mse.png`: Visual comparison of model error rates.
- Supporting scripts: `app.py`, `train_model.py`, `spotify_auth.py`

## 🧠 Features
- Exploratory Data Analysis (EDA)
- Data preprocessing and visualization
- Multiple model training: Linear, Random Forest, Decision Tree, Gradient Boosting, KNN
- Model evaluation using MSE and R²
- Interpretability discussion
- Final comparison table and chart

## 🚀 How to Run
1. Open this notebook in [Google Colab](https://colab.research.google.com/github/bedrock510/HitSense-Plus/blob/main/HitSense_EDA_and_Model_FULL_FINAL_WITH_CODE.ipynb)
2. Run each cell from top to bottom
3. Examine outputs and final comparison

## 📊 Final Model Comparison

| Model              | Description                 |
|-------------------|-----------------------------|
| Linear Regression | Simple, interpretable       |
| Random Forest     | High accuracy, less explainable |
| Decision Tree     | Fast but prone to overfit   |
| Gradient Boosting | Best performance overall    |
| KNN Regressor     | Simple non-parametric model |

## ✅ Key Findings
- Danceability and energy are most positively correlated with popularity
- Random Forest and Gradient Boosting yielded lowest Mean Squared Error
- Linear Regression was easiest to interpret, offering explainability for stakeholders

## 📬 Contact
Created by the HitSense Team  
For questions or collaboration, contact [bedrock510](https://github.com/bedrock510)
