class Usuario {
    constructor(nombre, edad, suscripcion) {
        this.nombre = nombre;
        this.edad = edad;
        this.suscripcion = suscripcion;
    }

    toString() {
        return `Nombre: ${this.nombre}, Edad: ${this.edad}, Suscripción: ${this.suscripcion}`;
    }
}

module.exports = Usuario;
