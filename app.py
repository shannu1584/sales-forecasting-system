%%writefile app.py

from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load('best_model.pkl')

@app.get("/")
def home():
    return {"message": "Forecast API Running"}

@app.get("/predict")
def predict():

    sample = pd.DataFrame({
        'lag_1':[100],
        'lag_7':[110],
        'lag_30':[120],
        'rolling_mean_7':[115],
        'rolling_std_7':[5],
        'month':[5],
        'dayofweek':[2]
    })

    prediction = model.predict(sample)

    return {
        "forecast": prediction.tolist()
    }
