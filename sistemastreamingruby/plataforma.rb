class Plataforma
    attr_accessor :nombre, :tipo_contenido, :numero_usuarios
  
    def initialize(nombre = "Nombre por defecto", tipo_contenido = "Contenido por defecto", numero_usuarios = 0)
      @nombre = nombre
      @tipo_contenido = tipo_contenido
      @numero_usuarios = numero_usuarios
    end
  
    def to_s
      "Nombre: #{@nombre}, Tipo de contenido: #{@tipo_contenido}, Número de usuarios: #{@numero_usuarios}"
    end
  end
  