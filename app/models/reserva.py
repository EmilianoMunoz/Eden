class Reserva:
    __tablename__ = 'reservas'
    __codigo = ''
    __fecha_inicio = ''
    __fecha_fin = ''
    __num_cabana = ''
    __codigo_cliente = ''

    @property
    def codigo(self)->str:
        return self.__codigo
    @codigo.setter
    def codigo(self, code:str):
        self.__codigo = code

    @property
    def fecha_inicio(self)->str:
        return self.__fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio:str):
        self.__fecha_inicio = fecha_inicio

    @property
    def fecha_fin(self)->str:
        return self.__fecha_fin
    @fecha_fin.setter
    def fecha_fin(self, fecha_fin:str):
        self.__fecha_fin = fecha_fin

    @property
    def num_cabana(self)->str:
        return self.__num_cabana
    @num_cabana.setter
    def num_cabana(self, num_cabana:str):
        self.__num_cabana = num_cabana

    @property
    def codigo_cliente(self)->str:
        return self.__codigo_cliente
    @codigo_cliente.setter
    def codigo_cliente(self, codigo_cliente:str):
        self.__codigo_cliente = codigo_cliente