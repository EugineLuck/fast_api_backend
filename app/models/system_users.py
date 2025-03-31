from sqlalchemy import Column, Integer, String
from app.models.base import Base

class SystemUser(Base):
    __tablename__ = "system_users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))