class Suscripcion {
    constructor(nombre = "Básica", precio = 0.00) {
        this.nombre = nombre;
        this.precio = precio;
    }

    toString() {
        return `Nombre: ${this.nombre}, Precio: $${this.precio}`;
    }
}

module.exports = Suscripcion;
