





from Database.DataBase import Database
from Entities import Category, Favorites
from Entities.User import Users


class FavoriteRepository():
    def __init__(self,Data):
        self.Data = Data
        
    def ValidFavorite(self,UsuId,checkUserId,CategoryId,checkCategoryId,UrlImage,Url):
        if not UrlImage:
            return False,'Url Imagem inválida.'
        if not Url:
            return False,'Url favorita é inválida.'
        Data = Database()
        if checkUserId:
            if not UsuId:
                return False,'Usuário inválido.'
            response = Data.DoSelect(Users,USUid=UsuId)
            if len(response) == 0:
                return False,'Usuário não encontrado.'
        if checkCategoryId:
            if not CategoryId:
                return False,'Categoria inválida.'
            response = Data.DoSelect(Category,CTid=CategoryId)
            if len(response) == 0:
                return False,'Categoria não encontrada.'
        return True
        
        
    def CreateFavorite(self):
        UrlContent = self.Data.get('urlContent')
        UsuId = self.Data.get('usuId')
        CategoryId = self.Data.get('categoryId')
        UrlImage = self.Data.get('urlImage')
        response,message = self.ValidFavorite(UsuId,True,CategoryId,True,UrlImage,UrlContent)
        if not response:
            return 400,message
        Data = Database()
        response = Data.DoInsert(Favorites,FVurl=UrlContent,FVusUId=UsuId,FVctId=CategoryId,FVurlImage=UrlImage)
        if response is None:
            return 400,'Ocorreu um erro ao inserir o registro, tente novamente.'
        return 200
    
    def DeleteFavorite(self):
        FavoriteId = self.Data.get('favoriteId')
        if not FavoriteId:
            return 400,"Favorito é inválido."
        Data = Database()
        response = Data.DoSelect(Favorites,FVid=FavoriteId)
        if len(response) == 0:
            return 400,"Favorito não encontrado."
        response = Data.DoDelete(Favorites,FVid=FavoriteId)
        if response is None:
            return 400,'Não foi encontrado o registro e não foi possíve deletar.'
        return 200
        
    def ListAllFavoriteForUser(self):
        UserId = self.Data.get('userId')
        if not UserId:
            return 400,'Usuário é inválido.'     
        Data = Database()
        userExist = Data.DoSelect(Users,USUid=UserId)
        if len(userExist) == 0:
            return 400, 'Usuário nao encontrado.'
        favoritesList = Data.DoSelect(Favorites,FVusUId=UserId)
        return 200,favoritesList
    
    def ListAFavorite(self):
        FavoriteId = self.Data.get('favoriteId')
        Data = Database()
        response = Data.DoSelect(Favorites,FVid=FavoriteId)
        return 200,response
    
    
    def UpdateFavorite(self):
        FavoriteId = self.Data.get('favoriteId')
        UrlContent = self.Data.get('urlContent')
        UsuId = self.Data.get('usuId')
        CategoryId = self.Data.get('categoryId')
        UrlImage = self.Data.get('urlImage')
        Data = Database()
        response = Data.DoSelect(Favorites,FVid=FavoriteId)
        if len(response) == 0:
            return 400,"Favorito não encontrado."
        response,message = self.ValidFavorite(UsuId,True,CategoryId,True,UrlImage,UrlContent)
        if not response:
            return 400,message
        Data.DoUpdate(Favorites,{'FVid':FavoriteId},{'FVctId':CategoryId,'FVurlImage':UrlImage,'FVurl':UrlContent})
        return 200
    
