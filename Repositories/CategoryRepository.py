from Database.DataBase import Database
from Entities.Category import Category

class CategoryRepository():
    def __init__(self,Data):
        self.Data = Data
        
    def ValidCategory(self,categoryName):
        if not categoryName:
            return False,'Categoria é inválida.'
        if len(categoryName) < 2:
            return False,'Categoria não atingiu o limite mínimo de caracteres que são 2.'
        return True
        
        
    def CreateCategory(self):
        categoryName = self.Data.get('category')
        response,message = self.ValidCategory(categoryName)
        if not response:
            return 400,message
        Data = Database()
        response = Data.DoInsert(Category,CTname=categoryName)
        if response is None:
            return 400,'Ocorreu um erro ao inserir o registro, tente novamente.'
        return 200
    
    def UpdateCategory(self):
        idCategory = self.Data.get('id')
        categoryName = self.Data.get('category')
        response,message = self.ValidCategory(categoryName)
        if not response:
            return 400,message
        Data = Database()
        listCategories = Data.DoSelect(Category,CTId=idCategory)
        if len(listCategories) == 0:
            return 400,'Não foi encontrado a categoria selecionada.'
        response = Data.DoUpdate(Category,{'CTId':idCategory},{'CTname':categoryName})
        if response is None:
            return 400,'Ocorreu um erro ao inserir o registro, tente novamente.'
        return 200
    
    def ListAllCategories(self):
        Data = Database()
        listCategories = Data.DoSelect(Category)
        if len(listCategories) == 0:
            return 400,'Não foi encontrado a categoria selecionada.' 
        return 200,listCategories
        