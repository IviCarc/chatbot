
const mostrarFechas = (fechasOcupadas) => {
  const currentDate = new Date();
  const oneWeekLater = new Date(currentDate.getTime() + 7 * 24 * 60 * 60 * 1000);
  const newInput = document.getElementById('fechaHora');

  newInput.innerHTML = '';

  let contador = 0;

  while (currentDate < oneWeekLater) {
    if (currentDate.getDay() >= 1 && currentDate.getDay() <= 5) {
      const option1Value = currentDate.toLocaleDateString('en-GB') + ' 14:00:00';
      if (!fechasOcupadas.includes(option1Value)) {
        const option1 = new Option(currentDate.toLocaleDateString('en-GB') + ' 14:00', option1Value)
        newInput.appendChild(option1);
      } else contador ++;
      const option2Value = currentDate.toLocaleDateString('en-GB') + ' 15:00:00';
      console.log(option2Value)
      if (!fechasOcupadas.includes(option2Value)) {
        const option2 = new Option(currentDate.toLocaleDateString('en-GB') + ' 15:00', option2Value)
        newInput.appendChild(option2);
      } else contador++
    }
    currentDate.setDate(currentDate.getDate() + 1);
  }

  // SI NO HAY REUNIONES DISPONIBLES
  if (contador == 10) {
    alert("todas ocupadas")
  }
  const fechaContainer = document.getElementById('fecha-container');

  // fechaContainer.appendChild(datalist);

  // newInput.setAttribute("list", "fechasDisponibles");
  newInput.setAttribute("id", "fechaHora");
  newInput.setAttribute("name", "fechaHora");
  // newInput.setAttribute("type", "datetime-local");
  newInput.classList.add("form-select");

  fechaContainer.appendChild(newInput);
}


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

  const botText = "¡Hola! Soy un bot de asistencia tecnica para el Laboratorio Consultar. ¿Que puedo hacer para ayudarte?";
  addBotMessage(botText);


  function processUserInput() {
    const message = userInput.value.trim();
    if (message === '') {
      return; // Evita enviar una solicitud vacía
    }

    if (message === "AGENDAR") {
      formulario.style.display = "block";
      chatBody.style.filter = 'blur(5px)'
      chatHeader.style.filter = 'blur(5px)'
      document.getElementById("user-input").style.display = "none";

      fetch("http://localhost:80/reuniones/fechas_ocupadas")
        .then(res => res.json())
        .then(res => mostrarFechas(res))
        .catch(err => console.log(err))

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


const mostrarBoton = document.getElementById("mostrarBoton");
const chatbotContainer = document.getElementById("chatbotContainer");

mostrarBoton.addEventListener("click", function () {
  chatbotContainer.style.display = "block";
  mostrarBoton.style.display = 'none';
});

var fechaHoraInput = document.getElementById('fechaHora');

// function actualizarLimites() {
//   var hoy = new Date();
//   hoy.setDate(hoy.getDate() + 1); // Establecer el día siguiente al día actual
//   var minDate = hoy.toISOString().slice(0, 16);
//   var maxDate = new Date(hoy.getTime() + 7 * 24 * 60 * 60 * 1000).toISOString().slice(0, 16);

//   fechaHoraInput.setAttribute('min', minDate);
//   fechaHoraInput.setAttribute('max', maxDate);
// }

// actualizarLimites();

// Actualizar los límites cada vez que pasa un día (cada 24 horas)
// setInterval(actualizarLimites, 24 * 60 * 60 * 1000);