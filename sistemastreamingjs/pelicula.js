class Pelicula {
    constructor(titulo = "PeliculaDefault", director = "DirectorDefault", duracion = 0) {
        this.titulo = titulo;
        this.director = director;
        this.duracion = duracion;
    }

    toString() {
        return `Título: ${this.titulo}, Director: ${this.director}, Duración: ${this.duracion} min`;
    }
}

module.exports = Pelicula;
