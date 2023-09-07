from app import db
from sqlalchemy.ext.hybrid import hybrid_property

class Administrador(db.Model):
    __tablename__ = 'administradores'
    __id = db.Column('id', db.Integer, primary_key=True)
    __codigo = db.Column('codigo', db.String(255))
    __nombre = db.Column('nombre', db.String(255))
    __puesto = db.Column('puesto', db.String(255))

    @hybrid_property
    def codigo(self)->str:
        return self.__codigo
    @codigo.setter
    def codigo(self, code:str):
        self.__codigo = code

    @hybrid_property
    def nombre(self)->str:
        return self.__nombre
    @nombre.setter
    def nombre(self, name:str):
        self.__nombre = name 

    @hybrid_property
    def puesto(self)->str:
        return self.__puesto
    @puesto.setter
    def puesto(self, title:str):
        self.__puesto = title