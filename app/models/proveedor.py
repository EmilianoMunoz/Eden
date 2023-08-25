class Proveedor:
    __tablename__: 'proveedores'
    
    __nombre = ''
    __codigo = ''
    __cuit = '' 
    __telefono = ''
    __email = ''
    __insumo = ''

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
    def cuit(self)->str:
        return self.__cuit
    @cuit.setter
    def cuit(self, cuit:str):
        self.__cuit = cuit

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
    def insumo(self)->str:
        return self.__insumo
    @insumo.setter
    def insumo(self, insumo:str):
        self.__insumo = insumo