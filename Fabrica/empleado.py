# CLASE EMPLEADO
class Empleado:
    def __init__(self, nombre, edad, cargo, turno, experiencia_anios):
        self.__nombre = nombre
        self.__edad = edad
        self.__cargo = cargo
        self.__turno = turno
        self.__experiencia_anios = experiencia_anios
      
    def get_nombre(self):
        return self.__nombre
 
    def get_edad(self):
        return self.__edad
 
    def get_cargo(self):
        return self.__cargo
 
    def get_turno(self):
        return self.__turno
 
    def get_experiencia_anios(self):
        return self.__experiencia_anios
 
    def set_nombre(self, nombre):
        self.__nombre = nombre
 
    def set_edad(self, edad):
        self.__edad = edad
 
    def set_cargo(self, cargo):
        self.__cargo = cargo
 
    def set_turno(self, turno):
        self.__turno = turno
 
    def set_experiencia_anios(self, anios):
        self.__experiencia_anios = anios

    def __str__(self):
        return "Empleado " + self.__nombre + " (" + str(self.__edad) + " anios) | " + self.__cargo + " | turno: " + self.__turno + " | experiencia: " + str(self.__experiencia_anios) + " anios"
 
    def supervisar(self, maquina):
        print(self.__nombre + " supervisa la " + maquina.get_modelo())
 
    def reportar(self, mensaje):
        print("[Reporte de " + self.__nombre + "] " + mensaje)
 
    def instalar_objeto(self, objeto, carro, maquina):
        if maquina.get_ocupada() == False:
            print("Primero hay que subir el carro a la maquina")
            return False
        if objeto.revisar() == False:
            return False
 
        print(self.__nombre + " instala " + objeto.get_nombre() + " en el " + carro.get_marca() + " " + carro.get_modelo() + "...")
        objeto.set_instalado(True)
        print("Objeto instalado correctamente")
        return True
