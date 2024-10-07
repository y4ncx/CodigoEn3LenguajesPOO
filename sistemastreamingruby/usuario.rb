class Usuario
    attr_accessor :nombre, :edad, :suscripcion
  
    def initialize(nombre, edad, suscripcion)
      @nombre = nombre
      @edad = edad
      @suscripcion = suscripcion
    end
  
    def to_s
      "Nombre: #{@nombre}, Edad: #{@edad}, Suscripción: #{@suscripcion}"
    end
  end
  