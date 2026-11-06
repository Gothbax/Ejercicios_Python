class Carro:
    def __init__(self, marca, modelo, color, velocidad, encendido):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__velocidad = velocidad
        self.__encendido = encendido

    def get_marca(self):
        return self.__marca
 
    def get_modelo(self):
        return self.__modelo
 
    def get_color(self):
        return self.__color
 
    def get_velocidad(self):
        return self.__velocidad
 
    def get_encendido(self):
        return self.__encendido
 
    # setters
    def set_marca(self, marca):
        self.__marca = marca
 
    def set_modelo(self, modelo):
        self.__modelo = modelo
 
    def set_color(self, color):
        self.__color = color
 
    def set_velocidad(self, velocidad):

        if velocidad < 0:
            self.__velocidad = 0
        else:
            self.__velocidad = velocidad
 
    def set_encendido(self, encendido):
        self.__encendido = encendido
