from app import db
from sqlalchemy.ext.hybrid import hybrid_property

class Cabana(db.Model):
    __id = db.Column('id', db.Integer, primary_key=True)
    __capacidad = db.Column('capacidad', db.String(255))
    __tipo = db.Column('tipo', db.String(255))
    __nivel = db.Column('nivel', db.String(255))
    __codigo = db.Column('codigo', db.String(255))

    @hybrid_property
    def codigo(self)->str:
        return self.__codigo
    @codigo.setter
    def codigo(self, code:str):
        self.__codigo = code    

    @hybrid_property
    def capacidad(self)->str:
        return self.__capacidad
    @capacidad.setter
    def capacidad(self, capacity:str):
        self.__capacidad = capacity

    @hybrid_property
    def tipo(self)->str:
        return self.__tipo
    @tipo.setter
    def tipo(self, type:str):
        self.__tipo = type

    @hybrid_property
    def nivel(self)->str:
        return self.__nivel
    @nivel.setter
    def nivel(self, level:str):
        self.__nivel = level