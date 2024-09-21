from Entities.Tags import Tags
from Database.DataBase import Database
from Entities.User import Users


class TagRepository():
    def __init__(self,Data):
        self.Data = Data
        
    def ValidTag(self,tagName,tagIdUser,checkUserId):
        if not tagName:
            return False,'Tag é inválida.'
        if len(tagName) < 2:
            return False,'Tag não atingiu o limite mínimo de caracteres que são 2.'
        if checkUserId:
            if not tagIdUser:
                return False,'Id Usuário é inválido.'
            Data = Database()
            UserExist = Data.DoSelect(Users,USUid=tagIdUser)
            if len(UserExist) == 0:
                return False,'Usuário não encontrado.'
        return True
        
    def CreateTag(self):
        tagName = self.Data.get('tagName')
        tagIdUser = self.Data.get('tagIdUser')
        response,message = self.ValidTag(tagName,tagIdUser,True)
        if not response:
            return 400,message
        Data = Database()
        response = Data.DoInsert(Tags,TGname=tagName,)
        if response is None:
            return 400,'Ocorreu um erro ao inserir o registro, tente novamente.'
        return 200
    
    def UpdateTag(self):
        idTag = self.Data.get('tagId')
        tagName = self.Data.get('tagName')
        response,message = self.ValidTag(tagName,0,False)
        if not response:
            return 400,message
        Data = Database()
        listTags = Data.DoSelect(Tags,TGid=idTag)
        if len(listTags) == 0:
            return 400,'Não foi encontrado a Tag selecionada.'
        response = Data.DoUpdate(Tags,{'TGid':idTag},{'TGname':tagName})
        if response is None:
            return 400,'Ocorreu um erro ao inserir o registro, tente novamente.'
        return 200
    
    def ListAllTagForUserId(self):
        tagIdUser = self.Data.get('tagIdUser')
        if not tagIdUser:
            return 400,'Id Usuário é inválido.'
        Data = Database()
        UserExist = Data.DoSelect(Users,USUid=tagIdUser)
        if len(UserExist) == 0:
            return 400, 'Usuário nao encontrado.'
        listTags = Data.DoSelect(Tags,TGIdUser=tagIdUser)
        return 200,listTags
    
    def DeleteTag(self):
        idTag = self.Data.get('tagId')
        Data = Database()
        tagExist = Data.DoSelect(Users,TGid=idTag)
        if len(tagExist) == 0:
            return 400, 'Tag não encontrada.'
        response = Data.DoDelete(Tags,TGid=idTag)
        if response is None:
            return 400,'Tag não encontrada.'
        return 200