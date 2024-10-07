class Plataforma:
    def __init__(self, nombre, tipoContenido, numeroUsuarios):
        
        self.__nombre = nombre
        self.__tipoContenido = tipoContenido
        self.__numeroUsuarios = numeroUsuarios

    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getTipoContenido(self):
        return self.__tipoContenido
    
    def setTipoContenido(self, tipoContenido):
        self.__tipoContenido = tipoContenido

    def getNumeroUsuarios(self):
        return self.__numeroUsuarios
    
    def setNumeroUsuarios(self, numeroUsuarios):
        self.__numeroUsuarios = numeroUsuarios
    
    
    def __str__(self):
        return f"Plataforma: {self.__nombre}, Tipo de contenido: {self.__tipoContenido}, Número de usuarios: {self.__numeroUsuarios}"
