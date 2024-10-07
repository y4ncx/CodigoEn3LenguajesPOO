from suscripcion import Suscripcion  

class Usuario:
    def __init__(self, nombre, edad, suscripcion):
        
        self.__nombre = nombre
        self.__edad = edad
        self.__suscripcion = suscripcion

   
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getEdad(self):
        return self.__edad
    
    def setEdad(self, edad):
        self.__edad = edad

    def getSuscripcion(self):
        return self.__suscripcion
    
    def setSuscripcion(self, suscripcion):
        self.__suscripcion = suscripcion
    
   
    def __str__(self):
        return f"Usuario: {self.__nombre}, Edad: {self.__edad}, {self.__suscripcion}"
