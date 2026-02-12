from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
from typing import List

app = FastAPI()

# Allow Chrome Extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage
tracked_products = []

class Product(BaseModel):
    title: str
    price: float

@app.post("/analyze")
def analyze_product(product: Product):

    # Generate fake historical data
    history = [round(product.price * random.uniform(0.9, 1.1), 2) for _ in range(7)]

    avg_price = sum(history) / len(history)

    volatility = max(history) - min(history)

    # Decision logic
    if product.price < avg_price * 0.95:
        decision = "BUY"
        confidence = random.randint(80, 95)
    elif product.price > avg_price * 1.05:
        decision = "WAIT"
        confidence = random.randint(65, 85)
    else:
        decision = "CONSIDER"
        confidence = random.randint(60, 75)

    drop_probability = random.randint(40, 80)

    explanation = f"Current price compared to 7-day average ₹{round(avg_price,2)}. Volatility level ₹{round(volatility,2)}."

    return {
        "decision": decision,
        "confidence": confidence,
        "history": history,
        "drop_probability": drop_probability,
        "explanation": explanation
    }

@app.post("/track")
def track_product(product: Product):
    tracked_products.append(product)
    return {"message": "Tracked successfully"}

@app.get("/portfolio")
def get_portfolio():
    return tracked_products

@app.get("/")
def root():
    return {"message": "PriceIntel api is live"}