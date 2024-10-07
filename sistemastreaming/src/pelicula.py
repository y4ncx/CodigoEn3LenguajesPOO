class Pelicula:
    def __init__(self, titulo, director, duracion):
        
        self.__titulo = titulo
        self.__director = director
        self.__duracion = duracion

    
    def getTitulo(self):
        return self.__titulo
    
    def setTitulo(self, titulo):
        self.__titulo = titulo

    def getDirector(self):
        return self.__director
    
    def setDirector(self, director):
        self.__director = director

    def getDuracion(self):
        return self.__duracion
    
    def setDuracion(self, duracion):
        self.__duracion = duracion
    
    
    def __str__(self):
        return f"Título: {self.__titulo}, Director: {self.__director}, Duración: {self.__duracion} minutos"
