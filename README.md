# sales-forecasting-system
# End-to-End Time Series Forecasting System

## Project Overview

This project implements a production-style time series forecasting system for predicting state-wise sales using historical sales data.

The system:
- Trains multiple forecasting models
- Performs feature engineering
- Automatically selects the best model
- Exposes predictions through REST API

---

## Dataset

Dataset contains:
- State
- Date
- Total Sales
- Category

---

## Models Implemented

1. SARIMA
2. Facebook Prophet
3. XGBoost
4. LSTM

---

## Feature Engineering

Implemented:
- Lag Features
- Rolling Mean
- Rolling Standard Deviation
- Month Feature
- Day of Week Feature

---

## Evaluation Metrics

Used:
- MAE
- RMSE
- MAPE

---

## Best Model Selection

The best model was automatically selected based on lowest RMSE.

---

## REST API

FastAPI was used to expose prediction endpoints.

### Endpoints

#### Home
GET /

#### Predict
GET /predict

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Prophet
- XGBoost
- TensorFlow
- FastAPI

---

## API Documentation

Swagger documentation available at:

/docs

---

## Results

The system successfully generated future sales forecasts and exposed predictions through REST APIs.

---

## Future Improvements

- Cloud deployment
- Real-time forecasting
- Advanced hyperparameter tuning
- Multi-state forecasting pipeline
