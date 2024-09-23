from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from Database.Base import Base

class Users(Base):
    __tablename__ = 'Users'
    
    USUid = Column(Integer, primary_key=True, autoincrement=True)
    USUsername = Column(String(256), nullable=False)
    USUpassword = Column(String(256), nullable=False)
    USUcreated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relacionamento com Favorites (um para muitos)
    favorites = relationship("Favorites", back_populates="user")
    
    # Relacionamento com Tags (um para muitos)
    tags = relationship("Tags", back_populates="user")
