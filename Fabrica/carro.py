# CLASE CARRO
class Carro:
    def __init__(self, marca, modelo, color, velocidad, encendido):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__velocidad = velocidad
        self.__encendido = encendido
 
    # getters
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
 
    # metodo __str__
    def __str__(self):
        if self.__encendido == True:
            estado = "encendido"
        else:
            estado = "apagado"
        return "Carro " + self.__marca + " " + self.__modelo + " | color: " + self.__color + " | velocidad: " + str(self.__velocidad) + " km/h | " + estado
 
    # metodos de funcionamiento
    def encender(self):
        if self.__encendido == True:
            print("El carro ya esta encendido")
        else:
            self.__encendido = True
            print("Motor encendido")
 
    def apagar(self):
        if self.__velocidad > 0:
            print("No se puede apagar en movimiento, frene primero")
        else:
            self.__encendido = False
            print("Motor apagado")
 
    def acelerar(self, incremento):
        if self.__encendido == False:
            print("Encienda el carro antes de acelerar")
        else:
            self.__velocidad = self.__velocidad + incremento
            print("Acelerando... velocidad: " + str(self.__velocidad) + " km/h")
 
    def frenar(self, decremento):
        self.__velocidad = self.__velocidad - decremento
        if self.__velocidad < 0:
            self.__velocidad = 0
        print("Frenando... velocidad: " + str(self.__velocidad) + " km/h")
 
    def girar(self, direccion):
        if self.__velocidad == 0:
            print("El carro esta detenido, no puede girar")
        else:
            print("Girando a la " + direccion)
