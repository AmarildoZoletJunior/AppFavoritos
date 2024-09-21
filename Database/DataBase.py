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
        self.engine = self.ConnectDataBase()
        if isinstance(self.engine, str):
            print(self.engine)
        else:
            self.Session = sessionmaker(bind=self.engine)
            self.VerifyBaseTables()

    def VerifyBaseTables(self):
        try:
            Base.metadata.create_all(self.engine, checkfirst=True)
        except Exception as e:
            print(f"Ocorreu um erro ao criar as tabelas do banco, verifique a conexão")
            print(str(e))

    def ConnectDataBase(self):
        try:
            params = urllib.parse.quote_plus(
                f"DRIVER={configuration.DRIVER};"
                f"SERVER={configuration.SERVER};"
                f"DATABASE={configuration.DATABASE};"
                f"Trusted_Connection=yes;"
            )
            engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}", echo=True)
            with engine.connect() as connection:
                pass
            return engine
        except Exception as e:
            error_message = f'Ocorreu um erro ao conectar-se ao banco de dados: {str(e)}'
            return error_message

    def DoSelect(self, model, **filters):
        if isinstance(self.engine, str):
            return []
        with self.Session() as session:
            query = session.query(model).filter_by(**filters)
            results = query.all()
            result_list = [self.objectToDict(result) for result in results]
            return result_list
        
    def objectToDict(self, obj):
        if obj is None:
            return None
        return {column.name: getattr(obj, column.name) for column in obj.__table__.columns}
    
    def DoInsert(self, model, **data):
        if isinstance(self.engine, str):
            return None
        with self.Session() as session:
            try:
                new_record = model(**data)
                session.add(new_record)
                session.commit()
                return self.objectToDict(new_record)
            except Exception as e:
                session.rollback()
                print(f"Erro ao inserir dados: {e}")
                return None
            
    def DoUpdate(self, model, filters: dict, update_data: dict):
        if isinstance(self.engine, str):
            return None
        
        with self.Session() as session:
            try:
                query = session.query(model).filter_by(**filters)
                updated_count = query.update(update_data, synchronize_session=False)
                session.commit()
                return updated_count
            except Exception as e:
                session.rollback()
                print(f"Erro ao atualizar dados: {e}")
                return None
            
            
    def DoDelete(self, model, **filters):
        if isinstance(self.engine, str):
            return None
        with self.Session() as session:
            try:
                query = session.query(model).filter_by(**filters)
                deleted_count = query.delete(synchronize_session=False)
                session.commit()
                return deleted_count
            except Exception as e:
                session.rollback()
                print(f"Erro ao deletar dados: {e}")
                return None
