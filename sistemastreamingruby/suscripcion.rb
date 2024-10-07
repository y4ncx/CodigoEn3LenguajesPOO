class Suscripcion
    attr_accessor :nombre, :precio
  
    def initialize(nombre = "Básica", precio = 0.00)
      @nombre = nombre
      @precio = precio
    end
  
    def to_s
      "Nombre: #{@nombre}, Precio: $#{@precio}"
    end
  end
  