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
            return False,message
        Data = Database()
        response = Data.DoInsert(Category,CTname=categoryName)
        if response is None:
            return False,'Ocorreu um erro ao inserir o registro, tente novamente.'
        return True
    
    def UpdateCategory(self):
        idCategory = self.Data.get('id')
        categoryName = self.Data.get('category')
        response,message = self.ValidCategory(categoryName)
        if not response:
            return False,message
        Data = Database()
        listCategories = Data.DoSelect(Category,CTId=idCategory)
        if len(listCategories) == 0:
            return False,'Não foi encontrado a categoria selecionada.'
        response = Data.DoUpdate(Category,CTname=categoryName)
        if response is None:
            return False,'Ocorreu um erro ao inserir o registro, tente novamente.'
        return True
    
    def ListAllCategories(self):
        Data = Database()
        listCategories = Data.DoSelect(Category)
        if len(listCategories) == 0:
            return False,'Não foi encontrado a categoria selecionada.' 
        return True,listCategories
        