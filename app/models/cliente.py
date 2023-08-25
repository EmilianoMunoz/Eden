class Cliente:
    __tablename__ = 'clientes'
    __nombre = ''
    __codigo = ''
    __email = ''
    __telefono = ''
    __ciudad = ''
    
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
    def email(self)->str:
        return self.__email
    @email.setter
    def email(self, email:str):
        self.__email = email

    @property
    def telefono(self)->str:
        return self.__telefono
    @telefono.setter
    def telefono(self, phone:str):
        self.__telefono = phone

    @property
    def ciudad(self)->str:
        return self.__ciudad
    @ciudad.setter
    def ciudad(self, city:str):
        self.__ciudad = city



    def __repr__(self) -> str:
        return f'User: code:{self.codigo}, nombre: {self.nombre}'
    
    def __eq__(self, __value: object) -> bool:
        return self.codigo == __value.codigo and self.nombre == __value.nombre