from sqlalchemy import create_engine,text, MetaData
from sqlalchemy.orm import sessionmaker
from Entities.Category import Category
from Entities.Excerpts import Excerpts
from Entities.Favorites import Favorites
from Entities.Tags import Tags
from Entities.TagsToFavorite import TagsToFavorite
from Entities.User import Users
from Database.Base import Base
from Config import configuration
import urllib


class Database:
    def __init__(self):
        self.ConnectDataBase()
    
    def VerifyBaseTables(self,engine):
        try:
            Base.metadata.create_all(engine,checkfirst=True)
        except Exception as e:
            print(f"Ocorreu um erro ao criar as tabelas do banco, verifique a conexão" )
            
            
    def ConnectDataBase(self):
        try:
            params = urllib.parse.quote_plus(f"DRIVER={configuration.DRIVER};"
                                    f"SERVER={configuration.SERVER};"
                                    f"DATABASE={configuration.DATABASE};"
                                    f"Trusted_Connection=yes;")  
            engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params),echo=True)
            self.VerificarTabelasBase(engine)
            return engine
        except Exception as e:        
            return 'Ocorreu um erro ao conectar-se ao banco de dados.'