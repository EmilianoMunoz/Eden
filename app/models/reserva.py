from app import db
from sqlalchemy.ext.hybrid import hybrid_property

class Reserva(db.Model):
    __tablename__ = 'reservas'

    __id = db.Column('id', db.Integer, primary_key=True)
    __codigo = db.Column('codigo', db.String(255))
    __fecha_inicio = db.Column('fecha_inicio', db.String(255))
    __fecha_fin = db.Column('fecha_fin', db.String(255))
    __num_cabana = db.Column('num_cabana', db.String(255))
    __codigo_cliente = db.Column('codigo_cliente', db.String(255))

    @hybrid_property
    def codigo(self)->str:
        return self.__codigo
    @codigo.setter
    def codigo(self, code:str):
        self.__codigo = code

    @hybrid_property
    def fecha_inicio(self)->str:
        return self.__fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio:str):
        self.__fecha_inicio = fecha_inicio

    @hybrid_property
    def fecha_fin(self)->str:
        return self.__fecha_fin
    @fecha_fin.setter
    def fecha_fin(self, fecha_fin:str):
        self.__fecha_fin = fecha_fin

    @hybrid_property
    def num_cabana(self)->str:
        return self.__num_cabana
    @num_cabana.setter
    def num_cabana(self, num_cabana:str):
        self.__num_cabana = num_cabana

    @hybrid_property
    def codigo_cliente(self)->str:
        return self.__codigo_cliente
    @codigo_cliente.setter
    def codigo_cliente(self, codigo_cliente:str):
        self.__codigo_cliente = codigo_cliente