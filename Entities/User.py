from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from Database.Base import Base

class Users(Base):
    __tablename__ = 'Users'
    USUid = Column(Integer, primary_key=True, autoincrement=True)
    USUsername = Column(String(256), nullable=False)
    USUpassword = Column(String(256), nullable=False)
    USUcreated_at = Column(TIMESTAMP, nullable=False)
    
    # Relationship
    favorites = relationship("Favorites", back_populates="user")