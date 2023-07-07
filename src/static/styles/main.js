document.addEventListener('DOMContentLoaded', () => {
  const chatBody = document.getElementById('chat-body');
  const chatHeader = document.getElementById("chat-header");
  const userInput = document.getElementById('user-input');

  function addUserMessage(message) {
    const userMessage = document.createElement('div');
    userMessage.classList.add('message', 'user-message');
    userMessage.textContent = message;
    chatBody.appendChild(userMessage);
  }


  function addBotMessage(message) {
    const botMessage = document.createElement('div');
    botMessage.classList.add('message', 'bot-message');
    botMessage.textContent = message;
    chatBody.appendChild(botMessage);
  }

  function processUserInput() {
    const message = userInput.value.trim();
    if (message === '') {
      return; // Evita enviar una solicitud vacía
    }

    if (message === "AGENDAR") {
      formulario.style.display = "block";
      chatBody.style.filter  = 'blur(5px)'
      chatHeader.style.filter  = 'blur(5px)'
      document.getElementById("user-input").style.display = "none";
    }


    addUserMessage(message);
    
    userInput.value = '';

    // Envía el mensaje al servidor Flask utilizando AJAX
    const formData = new FormData();
    formData.append('userInput', message);

    // fetch('/process', {
    //   method: 'POST',
    //   body: formData
    // })
    // .then(response => response.json())
    // .then(data => {
    //   const botMessage = data.botMessage;
    //   addBotMessage(botMessage);
    // })
    // .catch(error => {
    //   console.error('Error:', error);
    // });
  }

  userInput.addEventListener('keydown', (event) => {
    if (event.keyCode === 13) {
      event.preventDefault(); // Evita el comportamiento predeterminado (enviar formulario)
      processUserInput();
    }
  });
});


const mostrarBoton = document.getElementById("mostrarBoton");
const chatbotContainer = document.getElementById("chatbotContainer");

mostrarBoton.addEventListener("click", function () {
  chatbotContainer.style.display = "block";
  mostrarBoton.style.display = 'none';
});

var fechaHoraInput = document.getElementById('fechaHora');

function actualizarLimites() {
  var hoy = new Date();
  hoy.setDate(hoy.getDate() + 1); // Establecer el día siguiente al día actual
  var minDate = hoy.toISOString().slice(0, 16);
  var maxDate = new Date(hoy.getTime() + 7 * 24 * 60 * 60 * 1000).toISOString().slice(0, 16);

  fechaHoraInput.setAttribute('min', minDate);
  fechaHoraInput.setAttribute('max', maxDate);
}

actualizarLimites();

// Actualizar los límites cada vez que pasa un día (cada 24 horas)
setInterval(actualizarLimites, 24 * 60 * 60 * 1000);