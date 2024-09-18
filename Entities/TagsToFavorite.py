from sqlalchemy import Column, DateTime, Integer, ForeignKey, func
from sqlalchemy.orm import relationship
from Database.Base import Base


class TagsToFavorite(Base):
    __tablename__ = 'TagsToFavorite'
    
    TagId = Column(Integer, ForeignKey('Tags.TGid'), primary_key=True, nullable=False)
    FavoriteId = Column(Integer, ForeignKey('Favorites.FVid'), primary_key=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    tag = relationship("Tags", back_populates="tags_to_favorite")
    favorite = relationship("Favorites", back_populates="tags_to_favorite")