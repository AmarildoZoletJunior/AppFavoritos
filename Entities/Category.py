from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Database.Base import Base



class Category(Base):
    __tablename__ = 'Category'
    
    CTid = Column(Integer, primary_key=True, autoincrement=True)
    CTname = Column(String(550), nullable=False)


    favorites = relationship("Favorites", back_populates="category")








