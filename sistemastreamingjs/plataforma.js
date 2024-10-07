class Plataforma {
    constructor(nombre = "Nombre por defecto", tipoContenido = "Contenido por defecto", numeroUsuarios = 0) {
        this.nombre = nombre;
        this.tipoContenido = tipoContenido;
        this.numeroUsuarios = numeroUsuarios;
    }

    toString() {
        return `Nombre: ${this.nombre}, Tipo de contenido: ${this.tipoContenido}, Número de usuarios: ${this.numeroUsuarios}`;
    }
}

module.exports = Plataforma;
