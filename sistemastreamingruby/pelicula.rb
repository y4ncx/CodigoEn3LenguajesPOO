class Pelicula
    attr_accessor :titulo, :director, :duracion
  
    def initialize(titulo = "PeliculaDefault", director = "DirectorDefault", duracion = 0)
      @titulo = titulo
      @director = director
      @duracion = duracion
    end
  
    def to_s
      "Título: #{@titulo}, Director: #{@director}, Duración: #{@duracion} min"
    end
  end
  