const Plataforma = require('./plataforma');
const Pelicula = require('./pelicula');
const Usuario = require('./usuario');
const Suscripcion = require('./suscripcion');

const main = () => {
    console.log("Código: 7502410016");
    console.log("Nombre: YANCES SALGADO JASSIR SAID");
    console.log("**********************************💀**********************************\n");

    const suscripcionDefault = new Suscripcion("Básica", 0.00);
    const suscripcionPersonalizada = new Suscripcion("Premium", 10.99);

    const plataformaDefault = new Plataforma();
    const plataformaPersonalizada = new Plataforma("CineTodo", "Contenido Exclusivo", 0);

    const peliculaDefault = new Pelicula();
    const peliculaPersonalizada = new Pelicula("El Origen", "Christopher Nolan", 148);

    const usuario1 = new Usuario("Ana", 28, suscripcionDefault);
    const usuario2 = new Usuario("Luis", 30, suscripcionPersonalizada);

    plataformaPersonalizada.numeroUsuarios = 300000;

    console.log("PlataformaPorDefecto:");
    console.log(plataformaDefault.toString());
    console.log(usuario1.toString());
    console.log(peliculaDefault.toString());
    console.log(suscripcionDefault.toString());

    console.log("\n");

    console.log("PlataformaPersonalizada:");
    console.log(plataformaPersonalizada.toString());
    console.log(usuario2.toString());
    console.log(peliculaPersonalizada.toString());
    console.log(suscripcionPersonalizada.toString());
};

main();
