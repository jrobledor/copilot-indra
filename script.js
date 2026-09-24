const botonInspiracion = document.querySelector('#inspire-button');
const mensajeDeAccion = document.querySelector('#action-message');
const contadorDeClics = document.querySelector('#click-count');

const mensajesDeInspiracion = [
  'Empieza por una línea y deja que crezca.',
  'La curiosidad ya es un buen plan.',
  'Prueba algo pequeño. Después, vuelve a probar.',
  'Tu próxima idea puede empezar justo aquí.'
];

let numeroDeActivaciones = 0;

botonInspiracion.addEventListener('click', () => {
  numeroDeActivaciones += 1;
  contadorDeClics.textContent = String(numeroDeActivaciones);

  const indiceDelMensaje = (numeroDeActivaciones - 1) % mensajesDeInspiracion.length;
  mensajeDeAccion.textContent = mensajesDeInspiracion[indiceDelMensaje];
});

const agujaHora = document.querySelector('#hour-hand');
const agujaMinuto = document.querySelector('#minute-hand');
const agujaSegundo = document.querySelector('#second-hand');

function actualizarReloj() {
  const fechaActual = new Date();
  const segundos = fechaActual.getSeconds();
  const minutos = fechaActual.getMinutes() + segundos / 60;
  const horas = (fechaActual.getHours() % 12) + minutos / 60;

  agujaHora.style.transform = `rotate(${horas * 30}deg)`;
  agujaMinuto.style.transform = `rotate(${minutos * 6}deg)`;
  agujaSegundo.style.transform = `rotate(${segundos * 6}deg)`;
}

actualizarReloj();
setInterval(actualizarReloj, 1000);
