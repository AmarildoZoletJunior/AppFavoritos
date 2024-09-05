from tkinter.tix import MAX
from sqlalchemy import VARCHAR, Column, Integer, String, ForeignKey, Text, BLOB, TIMESTAMP
from sqlalchemy.orm import relationship
from Database.Base import Base

class Favorites(Base):
    __tablename__ = 'Favorites'
    
    FVid = Column(Integer, primary_key=True, autoincrement=True)
    FVurl = Column(String(256), nullable=False)
    FVusUId = Column(Integer, ForeignKey('Users.USUid'), nullable=False)
    FVctId = Column(Integer, ForeignKey('Category.CTid'), nullable=False)
    FVurlImage = Column(VARCHAR(MAX), nullable=False)
    FVcreated_at = Column(TIMESTAMP, nullable=False)

    user = relationship("Users", back_populates="favorites")
    category = relationship("Category", back_populates="favorites")
    excerpts = relationship("Excerpts", back_populates="favorite")
    tags_to_favorite = relationship("TagsToFavorite", back_populates="favorite")