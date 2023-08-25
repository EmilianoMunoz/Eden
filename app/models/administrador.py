class Administrador:
__tablename__ = 'administradores'
__nombre = ''
__codigo = ''
__puesto = ''

@property
def codigo(self)->str:
    return self.__codigo
@codigo.setter
def codigo(self, code:str):
    self.__codigo = code

@property
def nombre(self)->str:
    return self.__nombre
@nombre.setter
def nombre(self, name:str):
    self.__nombre = name 

@property
def puesto(self)->str:
    return self.__puesto
@puesto.setter
def puesto(self, title:str):
    self.__puesto = title