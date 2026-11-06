# CLASE OBJETO 
class Objeto:
    def __init__(self, nombre, material, peso_kg, precio, instalado):
        self.__nombre = nombre
        self.__material = material
        self.__peso_kg = peso_kg
        self.__precio = precio
        self.__instalado = instalado
 
    def get_nombre(self):
        return self.__nombre
 
    def get_material(self):
        return self.__material
 
    def get_peso_kg(self):
        return self.__peso_kg
 
    def get_precio(self):
        return self.__precio
 
    def get_instalado(self):
        return self.__instalado
 
    def set_nombre(self, nombre):
        self.__nombre = nombre
 
    def set_material(self, material):
        self.__material = material
 
    def set_peso_kg(self, peso_kg):
        self.__peso_kg = peso_kg
 
    def set_precio(self, precio):
        self.__precio = precio
 
    def set_instalado(self, instalado):
        self.__instalado = instalado
 
    def __str__(self):
        if self.__instalado == True:
            estado = "instalado"
        else:
            estado = "sin instalar"
        return "Objeto " + self.__nombre + " | material: " + self.__material + " | peso: " + str(self.__peso_kg) + " kg | precio: $" + str(self.__precio) + " | " + estado
 
    def calcular_precio_con_iva(self):
        total = self.__precio + (self.__precio * 0.19)
        return total
 
    def revisar(self):
        if self.__peso_kg > 0 and self.__precio > 0:
            print("Revision del objeto: APROBADO")
            return True
        else:
            print("Revision del objeto: RECHAZADO (datos invalidos)")
            return False
 
