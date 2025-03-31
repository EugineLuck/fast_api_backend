from sqlalchemy import Column, Integer, String
from app.models.base import Base

class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    unique_id = Column(String(255))
