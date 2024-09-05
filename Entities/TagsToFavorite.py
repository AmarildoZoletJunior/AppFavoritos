from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from Database.Base import Base


class TagsToFavorite(Base):
    __tablename__ = 'TagsToFavorite'
    
    TagId = Column(Integer, ForeignKey('Tags.TGid'), primary_key=True, nullable=False)
    FavoriteId = Column(Integer, ForeignKey('Favorites.FVid'), primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    
    tag = relationship("Tags", back_populates="tags_to_favorite")
    favorite = relationship("Favorites", back_populates="tags_to_favorite")