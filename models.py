from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
import datetime

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    url = Column(String)
    image = Column(String)
    platform = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class PriceHistory(Base):
    __tablename__ = "price_history"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    price = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
