from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Database.Base import Base

class Tags(Base):
    __tablename__ = 'Tags'
    
    TGid = Column(Integer, primary_key=True, autoincrement=True)
    TGname = Column(String(256), nullable=False)
    TGIdUser = Column(Integer, ForeignKey('Users.USUid'), nullable=False)
    
    # Relacionamento com a tabela Users
    user = relationship("Users", back_populates="tags")
    
    # Relacionamento com a tabela de associação TagsToFavorite
    tags_to_favorite = relationship("TagsToFavorite", back_populates="tag")
