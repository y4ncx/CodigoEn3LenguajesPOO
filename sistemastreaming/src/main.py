from plataforma import Plataforma
from pelicula import Pelicula
from usuario import Usuario
from suscripcion import Suscripcion 

def main():
    
    print("Código: 7502410016")  
    print("Nombre: YANCES SALGADO JASSIR SAID")  
    print("**********************************\U0001F480**********************************\n")  

    
    suscripcion_default = Suscripcion("Básica", 0.00)  
    suscripcion_personalizada = Suscripcion("Premium", 10.99)

    
    plataforma_default = Plataforma("Nombre por defecto", "Contenido por defecto", 0)
    
    
    plataforma_personalizada = Plataforma("CineTodo", "Contenido Exclusivo", 0)

    
    pelicula_default = Pelicula("PeliculaDefault", "DirectorDefault", 0)  
    pelicula_personalizada = Pelicula("El Origen", "Christopher Nolan", 148)


    usuario1 = Usuario("Ana", 28, suscripcion_default)
    usuario2 = Usuario("Luis", 30, suscripcion_personalizada)

    
    plataforma_personalizada.setNumeroUsuarios(300000)

    
    print("PlataformaPorDefecto:")
    print(plataforma_default)
    print(usuario1)
    print(pelicula_default)
    print(suscripcion_default)

    print("\n")  

    
    print("PlataformaPersonalizada:")
    print(plataforma_personalizada)
    print(usuario2)
    print(pelicula_personalizada)
    print(suscripcion_personalizada)

if __name__ == "__main__":
    main()
