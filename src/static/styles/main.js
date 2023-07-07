document.addEventListener('DOMContentLoaded', () => {
  const chatBody = document.getElementById('chat-body');
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

  const botText = "¡Hola! Soy un bot de asistencia tecnica para el Laboratorio Consultar. ¿Que puedo hacer para ayudarte?";
  addBotMessage(botText);


  function processUserInput() {
    const message = userInput.value.trim();
    if (message === '') {
      return; // Evita enviar una solicitud vacía
    }

    if (message === "AGENDAR") {
      formulario.style.display = "block";
      document.getElementById("user-input").style.display = "none";
      return;
    }


    addUserMessage(message);
    userInput.value = '';
    
    // addBotMessage(botMessage)
    // chatBody.value = '';

    // Envía el mensaje al servidor Flask utilizando AJAX
    const formData = new FormData();
    formData.append('userInput', message);

    fetch('/process', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      const botMessage = data.botMessage;

      console.log(botMessage)
      addBotMessage(botMessage);
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }

  userInput.addEventListener('keydown', (event) => {
    if (event.keyCode === 13) {
      event.preventDefault(); // Evita el comportamiento predeterminado (enviar formulario)
      processUserInput();
      document.getElementById("form").reset();
      document.getElementById("user-input").value = '';
    }
  });
});
