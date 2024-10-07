require_relative 'plataforma'
require_relative 'pelicula'
require_relative 'usuario'
require_relative 'suscripcion'

def main
  
  puts "Código: 7502410016" 
  puts "Nombre: YANCES SALGADO JASSIR SAID"  
  puts "**********************************💀**********************************\n"

  
  suscripcion_default = Suscripcion.new("Básica", 0.00)  
  suscripcion_personalizada = Suscripcion.new("Premium", 10.99)

 
  plataforma_default = Plataforma.new
  
  
  plataforma_personalizada = Plataforma.new("CineTodo", "Contenido Exclusivo", 0)

  
  pelicula_default = Pelicula.new
  pelicula_personalizada = Pelicula.new("El Origen", "Christopher Nolan", 148)

  
  usuario1 = Usuario.new("Ana", 28, suscripcion_default)
  usuario2 = Usuario.new("Luis", 30, suscripcion_personalizada)

  
  plataforma_personalizada.numero_usuarios = 300000

  
  puts "PlataformaPorDefecto:"
  puts plataforma_default
  puts usuario1
  puts pelicula_default
  puts suscripcion_default

  puts "\n"  

  
  puts "PlataformaPersonalizada:"
  puts plataforma_personalizada
  puts usuario2
  puts pelicula_personalizada
  puts suscripcion_personalizada
end

main if __FILE__ == $0
