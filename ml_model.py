import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

def train_model(prices):
    X = np.arange(len(prices)).reshape(-1, 1)
    y = np.array(prices)

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, "price_model.pkl")
    return model

def predict_next(prices):
    model = train_model(prices)
    next_day = np.array([[len(prices)]])
    prediction = model.predict(next_day)
    return float(prediction[0])
