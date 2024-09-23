from Database.DataBase import Database

from Entities.Excerpts import Excerpts
from Entities.Favorites import Favorites


class ExcerptRepository():
    def __init__(self,Data):
        self.Data = Data
        
    def ValidExcerpt(self,ETExcerpts,ETfvId,checkFavorite):
        if not ETExcerpts:
            return False,'Comentário é inválido.'
        if len(ETExcerpts) < 2:
            return False,'Comentário não atingiu o limite mínimo de caracteres que são 2.'
        if checkFavorite:
            if not ETfvId:
                return False,'Favorito é inválido.'
            Data = Database()
            response = Data.DoSelect(Favorites,FVid=ETfvId)
            if len(response) == 0:
                return False,'Favorito não encontrado.'
        return True,''
        
    def CreateExcerpt(self):
        ExcerptContent = self.Data.get('ExcerptContent')
        idFavorito = self.Data.get('idFavorito')
        response,message = self.ValidExcerpt(ExcerptContent,idFavorito,True)
        if not response:
            return 400,message
        Data = Database()
        response = Data.DoInsert(Excerpts,ETExcerpts=ExcerptContent,ETfvId=idFavorito)
        if response is None:
            return 400,'Ocorreu um erro ao inserir o registro, tente novamente.'
        return 200,''

    def UpdateExcerpt(self):
        idExcerpt = self.Data.get('idExcerpt')
        ExcerptContent = self.Data.get('ExcerptContent')
        response,message = self.ValidExcerpt(ExcerptContent,0,False)
        if not response:
            return 400,message
        Data = Database()
        listExcerpts = Data.DoSelect(Excerpts,ETid=idExcerpt)
        if len(listExcerpts) == 0:
            return 400,'Não foi encontrado o comentário selecionado.'
        response = Data.DoUpdate(Excerpts,{'ETid':idExcerpt},{'ETExcerpts':ExcerptContent})
        if response is None:
            return 400,'Ocorreu um erro ao inserir o registro, tente novamente.'
        return 200,''
    
    def ListExcerptsOfFavorite(self):
        idFavorite = self.Data.get('idFavorite')
        if not idFavorite:
            return 400,'Não foi encontrado o favorito selecionado.'
        Data = Database()
        favoriteExist = Data.DoSelect(Favorites,FVid = idFavorite)
        if len(favoriteExist) == 0:
            return 400,'Não foi encontrado o favorito selecionado.' 
        listExcerpts = Data.DoSelect(Excerpts,ETfvId = idFavorite)
        return 200,listExcerpts
    
        
        
    def DeleteExcerpt(self):
        idExcerpt = self.Data.get('idExcerpt')
        if not idExcerpt:
            return 400,"Comentário é inválido."
        Data = Database()
        response = Data.DoSelect(Excerpts,ETid=idExcerpt)
        if len(response) == 0:
            return 400,"Comentário não encontrado."
        response = Data.DoDelete(Excerpts,ETid=idExcerpt)
        if response is None:
            return 400,'Não foi encontrado o registro e não foi possíve deletar.'
        return 200,''
        