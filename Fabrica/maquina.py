class Maquina:
    def __init__(self, modelo, capacidad_kg, altura_cm, encendida, ocupada):
        self.__modelo = modelo
        self.__capacidad_kg = capacidad_kg
        self.__altura_cm = altura_cm
        self.__encendida = encendida
        self.__ocupada = ocupada

    def get_modelo(self):
        return self.__modelo
 
    def get_capacidad_kg(self):
        return self.__capacidad_kg
 
    def get_altura_cm(self):
        return self.__altura_cm
 
    def get_encendida(self):
        return self.__encendida
 
    def get_ocupada(self):
        return self.__ocupada
 
    def set_modelo(self, modelo):
        self.__modelo = modelo
 
    def set_capacidad_kg(self, capacidad_kg):
        self.__capacidad_kg = capacidad_kg
 
    def set_altura_cm(self, altura_cm):
        self.__altura_cm = altura_cm
 
    def set_encendida(self, encendida):
        self.__encendida = encendida
 
    def set_ocupada(self, ocupada):
        self.__ocupada = ocupada

    def __str__(self):
        if self.__encendida == True:
            estado = "encendida"
        else:
            estado = "apagada"
        return "Maquina " + self.__modelo + " | capacidad: " + str(self.__capacidad_kg) + " kg | altura: " + str(self.__altura_cm) + " cm | " + estado
 
    def encender(self):
        self.__encendida = True
        print("Maquina encendida")
 
    def apagar(self):
        if self.__ocupada == True:
            print("Baje el carro antes de apagar la maquina")
        else:
            self.__encendida = False
            print("Maquina apagada")
 
    def subir_carro(self, carro):
        if self.__encendida == False:
            print("Encienda la maquina primero")
            return False
        if carro.get_encendido() == True:
            print("Seguridad: el carro debe estar apagado para subirlo")
            return False
        if self.__ocupada == True:
            print("La maquina ya tiene un carro arriba")
            return False
 
        self.__ocupada = True
        print("La maquina levanta el " + carro.get_marca() + " " + carro.get_modelo() + " a " + str(self.__altura_cm) + " cm")
        return True
 
    def bajar_carro(self, carro):
        if self.__ocupada == False:
            print("No hay ningun carro arriba")
        else:
            self.__ocupada = False
            print("La maquina baja el " + carro.get_marca() + " " + carro.get_modelo())
