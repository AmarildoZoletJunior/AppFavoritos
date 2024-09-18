from sqlalchemy import Column, DateTime, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from Database.Base import Base
from sqlalchemy.sql import func

class Users(Base):
    __tablename__ = 'Users'
    USUid = Column(Integer, primary_key=True, autoincrement=True)
    USUsername = Column(String(256), nullable=False)
    USUpassword = Column(String(256), nullable=False)
    USUcreated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    favorites = relationship("Favorites", back_populates="user")