from sqlalchemy import Column, Integer, String, ForeignKey, Text, BLOB, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Database.Base import Base


class Excerpts(Base):
    __tablename__ = 'Excerpts'
    
    ETid = Column(Integer, primary_key=True, autoincrement=True)
    ETfvId = Column(Integer, ForeignKey('Favorites.FVid'), nullable=False)
    ETExcerpts = Column(String(550), nullable=False)
    ETcreated_at = Column(TIMESTAMP, nullable=False)
    
    # Relationship
    favorite = relationship("Favorites", back_populates="excerpts")
    
    