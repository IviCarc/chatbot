// Obtén el elemento del formulario por su ID
const formulario = document.getElementById("formulario");
const chatBody = document.getElementById('chat-body');
const chatHeader = document.getElementById("chat-header");
// Función para mostrar el formulario
function mostrarFormulario() {
  console.log("FORM")
  formulario.style.display = "block";
}

// Función para ocultar el formulario
function ocultarFormulario() {
  formulario.style.display = "none";
  chatBody.style.filter  = 'blur(0px)'
  chatHeader.style.filter  = 'blur(0px)'
  document.getElementById("user-input").style.display = "block";
}

const phoneInputField = document.querySelector("#phone");
const phoneInput = window.intlTelInput(phoneInputField, {
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

// Escucha el evento de envío del formulario
formulario.addEventListener("submit", function(event) {
  event.preventDefault(); 

  let formData = new FormData(document.getElementById("form"));

  if (!process()) return // Si el teléfono es inválido, no envía el form

  formData.append('chat', "adad")
  // formData.append('fechaHora', formData.get('fechaHora').replace("T", " "))
  formData.set('fechaHora', formData.get('fechaHora').replace("T", " "))
  console.log(formData.getAll("fechaHora"))
  fetch("http://localhost:80/", {method:"POST", body: formData})
  .then(res => res.text())
  .then(res => res.json())
  .catch(err => console.log(err))

  // let config = {
  //   method: 'PUT',
  //   headers: { "Content-Type": "application/json" },
  // }

  // console.log("Formulario enviado");
  ocultarFormulario(); // Oculta el formulario después de enviarlo
});
