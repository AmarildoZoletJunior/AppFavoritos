from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from Database.Base import Base

class Tags(Base):
    __tablename__ = 'Tags'
    
    TGid = Column(Integer, primary_key=True, autoincrement=True)
    TGname = Column(String(256), nullable=False)
    TGIdUser = Column(Integer,ForeignKey('Users.USUid'),nullable= False)
    
    tags_to_favorite = relationship("TagsToFavorite", back_populates="tag")
    user = relationship("Users", back_populates="users_to_tags")