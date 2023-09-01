from app import db
from sqlalchemy.ext.hybrid import hybrid_property

class Cliente(db.Model):
    __tablename__ = 'clientes'
    __id = db.Column(db.Integer, primary_key=True)
    __nombre = db.Column(db.String(255))
    __codigo = db.Column(db.String(255))
    __email = db.Column(db.String(255))
    __telefono = db.Column(db.String(255))
    __ciudad = db.Column(db.String(255))
    
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
    def email(self)->str:
        return self.__email
    @email.setter
    def email(self, email:str):
        self.__email = email

    @hybrid_property
    def telefono(self)->str:
        return self.__telefono
    @telefono.setter
    def telefono(self, phone:str):
        self.__telefono = phone

    @hybrid_property
    def ciudad(self)->str:
        return self.__ciudad
    @ciudad.setter
    def ciudad(self, city:str):
        self.__ciudad = city



    def __repr__(self) -> str:
        return f'User: code:{self.codigo}, nombre: {self.nombre}'
    
    def __eq__(self, __value: object) -> bool:
        return self.codigo == __value.codigo and self.nombre == __value.nombre