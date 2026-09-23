const inspireButton = document.querySelector('#inspire-button');
const actionMessage = document.querySelector('#action-message');
const clickCount = document.querySelector('#click-count');

const messages = [
  'Empieza por una línea y deja que crezca.',
  'La curiosidad ya es un buen plan.',
  'Prueba algo pequeño. Después, vuelve a probar.',
  'Tu próxima idea puede empezar justo aquí.'
];

let activations = 0;

inspireButton.addEventListener('click', () => {
  activations += 1;
  clickCount.textContent = activations;
  actionMessage.textContent = messages[(activations - 1) % messages.length];
});

const hourHand = document.querySelector('#hour-hand');
const minuteHand = document.querySelector('#minute-hand');
const secondHand = document.querySelector('#second-hand');

function updateClock() {
  const now = new Date();
  const seconds = now.getSeconds();
  const minutes = now.getMinutes() + seconds / 60;
  const hours = (now.getHours() % 12) + minutes / 60;

  hourHand.style.transform = `rotate(${hours * 30}deg)`;
  minuteHand.style.transform = `rotate(${minutes * 6}deg)`;
  secondHand.style.transform = `rotate(${seconds * 6}deg)`;
}

updateClock();
setInterval(updateClock, 1000);
