from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Database.Base import Base

class Tags(Base):
    __tablename__ = 'Tags'
    
    TGid = Column(Integer, primary_key=True, autoincrement=True)
    TGname = Column(String(256), nullable=False)
    
    tags_to_favorite = relationship("TagsToFavorite", back_populates="tag")