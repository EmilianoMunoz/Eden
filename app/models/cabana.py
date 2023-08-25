class Cabana:
    __capacidad = ''
    __tipo = ''
    __nivel = ''
    __codigo = ''

    @property
    def codigo(self)->str:
        return self.__codigo
    @codigo.setter
    def codigo(self, code:str):
        self.__codigo = code    

    @property
    def capacidad(self)->str:
        return self.__capacidad
    @capacidad.setter
    def capacidad(self, capacity:str):
        self.__capacidad = capacity

    @property
    def tipo(self)->str:
        return self.__tipo
    @tipo.setter
    def tipo(self, type:str):
        self.__tipo = type

    @property
    def nivel(self)->str:
        return self.__nivel
    @nivel.setter
    def nivel(self, level:str):
        self.__nivel = level