from app import db
from sqlalchemy.ext.hybrid import hybrid_property

class Proveedor(db.Model):
    __tablename__: 'proveedores'
    
    __id = db.Column('id', db.Integer, primary_key=True)
    __nombre = db.Column('nombre', db.String(255))
    __codigo = db.Column('codigo', db.String(255))
    __cuit = db.Column('cuit', db.String(255))
    __telefono = db.Column('telefono', db.String(255))
    __email = db.Column('email', db.String(255))
    __insumo = db.Column('insumo', db.String(255))

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
    def cuit(self)->str:
        return self.__cuit
    @cuit.setter
    def cuit(self, cuit:str):
        self.__cuit = cuit

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
    def insumo(self)->str:
        return self.__insumo
    @insumo.setter
    def insumo(self, insumo:str):
        self.__insumo = insumo