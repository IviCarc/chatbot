const chatBody = document.getElementById('chat-body');
const chatHeader = document.getElementById("chat-header");
const userInput = document.getElementById('user-input');

// Obtén el elemento del formulario por su ID
const formContainer = document.getElementById("formulario-container");

// BOTON INICIAL //
const mostrarBoton = document.getElementById("mostrarBoton");
const chatbotContainer = document.getElementById("chatbotContainer");

mostrarBoton.addEventListener("click", function () {
	chatbotContainer.style.display = "block";
	mostrarBoton.style.display = 'none';
});

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

const botText1 = "¡Hola! Soy un bot de asistencia tecnica para el Laboratorio Consultar. ¿Que puedo hacer para ayudarte?";
addBotMessage(botText1);
const botText2 = "Si solo quieres agendar una reunion, escribe 'AGENDAR'";
addBotMessage(botText2);


function processUserInput() {
	const message = userInput.value.trim();
	if (message === '') {
		return; // Evita enviar una solicitud vacía
	}

	if (message === "AGENDAR") {
		mostrarFormulario();
		return;
	}


	addUserMessage(message);
	userInput.value = '';

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



// TELEFONO //

const phoneInputField = document.querySelector("#phone");
const phoneInput = window.intlTelInput(phoneInputField, {
	preferredCountries: ["ar", "uy", "cl", "py", "bo", "br"],
	utilsScript:
		"https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
});

const info = document.querySelector(".alert-info");
const error = document.querySelector(".alert-error");

function process(event) {
	const phoneNumber = phoneInput.getNumber();
	console.log(phoneNumber)
	info.style.display = "none";
	error.style.display = "none";

	if (phoneInput.isValidNumber()) {
		info.style.display = "block";
		info.innerHTML = `Número válido ✔️ `;
		phoneInputField.value = phoneNumber
		return true
	} else {
		error.style.display = "block";
		error.innerHTML = `Número inválido ❌.`;
		return false
	}
}

formContainer.addEventListener("submit", function (event) {
	event.preventDefault();

	let formData = new FormData(document.getElementById("form"));

	if (!process()) return // Si el teléfono es inválido, no envía el form

	formData.append('chat', "adad")
	formData.set('fechaHora', formData.get('fechaHora').replace("T", " "))
	console.log(formData.getAll("fechaHora"))
	fetch("http://localhost:80/", { method: "POST", body: formData })
		.then(res => res.text())
		.then(res => res.json())
		.catch(err => console.log(err))

	ocultarFormulario(); // Oculta el formulario después de enviarlo
});

// Mostrar fechas disponibles //

const mostrarFechas = (fechasOcupadas) => {
	const currentDate = new Date();
	const oneWeekLater = new Date(currentDate.getTime() + 7 * 24 * 60 * 60 * 1000);
	const newInput = document.getElementById('fechaHora');

	newInput.innerHTML = '';

	let cantFechasOcupadas = 0;
	while (currentDate < oneWeekLater) {
		if (currentDate.getDay() >= 1 && currentDate.getDay() <= 5) {
			const option1Value = currentDate.toLocaleDateString('en-GB') + ' 14:00:00';
			if (!fechasOcupadas.includes(option1Value)) {
				const option1 = new Option(currentDate.toLocaleDateString('en-GB') + ' 14:00', option1Value)
				newInput.appendChild(option1);
			} else cantFechasOcupadas++;

			const option2Value = currentDate.toLocaleDateString('en-GB') + ' 15:00:00';
			if (!fechasOcupadas.includes(option2Value)) {
				const option2 = new Option(currentDate.toLocaleDateString('en-GB') + ' 15:00', option2Value)
				newInput.appendChild(option2);
			}  else {
				cantFechasOcupadas++
			}
		}
		currentDate.setDate(currentDate.getDate() + 1);
	}

	// SI NO HAY REUNIONES DISPONIBLES
	if (cantFechasOcupadas >= 10) {
		// alert("todas ocupadas")
		addBotMessage("Lo lamento, no tenemos horarios disponibles. Si requieres atención, envía un mail a consultar@consultar.org. Puedes seguir haciendome consultas");
		ocultarFormulario();
	}
	const fechaContainer = document.getElementById('fecha-container');

	newInput.setAttribute("id", "fechaHora");
	newInput.setAttribute("name", "fechaHora");
	newInput.classList.add("form-select");

	fechaContainer.appendChild(newInput);
}

const mostrarFormulario = () => {
	fetch("http://localhost:80/reuniones/fechas_ocupadas")
		.then(res => res.json())
		.then(res => mostrarFechas(res))
		.catch(err => console.log(err))

	document.getElementById("user-input").style.display = "none";

	formContainer.classList.remove('form-container-invisible');
	formContainer.classList.add('form-container-visible');


}

const ocultarFormulario = () => {
	formContainer.classList.remove('form-container-visible');
	formContainer.classList.add('form-container-invisible');

	document.getElementById("user-input").style.display = "block";

	info.style.display = "none"
	error.style.display = "none"
}