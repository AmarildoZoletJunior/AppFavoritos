from Entities import Favorites, TagsToFavorite
from Entities.Tags import Tags
from Database.DataBase import Database


class TagToFavoriteRepository():
    def __init__(self,Data):
        self.Data = Data
        
    def ValidTagAndFavorite(self,tagId,FavoriteId):
        if not tagId:
            return False,'Tag é inválida.'
        if not FavoriteId:
            return False,'Favorito é inválido.'
        Data = Database()
        response = Data.DoSelect(Tags,TGid = tagId)
        if len(response) == 0:
            return False,'Tag não encontrada.' 
        response = Data.DoSelect(Favorites,FVid = FavoriteId)
        if len(response) == 0:
            return False,'Favorito não encontrado.' 
        return True
        
    def CreateTagAndFavorite(self):
        tagId = self.Data.get('tagId')
        FavoriteId = self.Data.get('FavoriteId')
        response,message = self.ValidTagAndFavorite(tagId,FavoriteId)
        if not response:
            return 400,message
        Data = Database()
        response = Data.DoInsert(Tags,FavoriteId=FavoriteId,TagId=tagId)
        if response is None:
            return 400,'Ocorreu um erro ao inserir o registro, tente novamente.'
        return 200
    
    def ListAllTagForTag(self):
        tagId = self.Data.get('tagId')
        if not tagId:
            return 400,'Tag é inválida.'
        Data = Database()
        TagExist = Data.DoSelect(Tags,TGid=tagId)
        if len(TagExist) == 0:
            return 400, 'Tag nao encontrada.'
        listFavoritesWithTag = Data.DoSelect(Tags,TagId=tagId)
        return 200,listFavoritesWithTag
    
    def DeleteTagAndFavorite(self):
        tagId = self.Data.get('tagId')
        FavoriteId = self.Data.get('FavoriteId')
        response,message = self.ValidTagAndFavorite(tagId,FavoriteId)
        if not response:
            return 400,message
        Data = Database()
        response = Data.DoDelete(TagsToFavorite,TagId=tagId,FavoriteId = FavoriteId)
        if response is None:
            return 400,'Não foi encontrado o registro.'
        return 200