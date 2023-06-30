// Obtén el elemento del formulario por su ID
const formulario = document.getElementById("formulario");

// Función para mostrar el formulario
function mostrarFormulario() {
  formulario.style.display = "block";
}

// var fechaHoraInput = document.getElementById('fechaHora');


// Función para ocultar el formulario
function ocultarFormulario() {
  formulario.style.display = "none";
  document.getElementById("myDIV").style.display = "block";
}

// Escucha el evento de envío del formulario
// formulario.addEventListener("submit", function(event) {
  
//   event.preventDefault(); // Evita que se recargue la página al enviar el formulario
//   // Aquí puedes agregar la lógica para procesar los datos del formulario y agendar la reunión
//   // Por ejemplo, puedes obtener los valores de los campos de entrada usando:
//   // const nombre = document.getElementById("nombre").value;
//   // const fecha = document.getElementById("fecha").value;
//   // const hora = document.getElementById("hora").value;
//   // Y luego puedes enviar los datos a través de una solicitud al servidor o realizar otras acciones necesarias
//   console.log("Formulario enviado");
//   ocultarFormulario(); // Oculta el formulario después de enviarlo
// });

// Ejemplo de cómo invocar la función para mostrar el formulario en respuesta a un comando
const comando = document.getElementById("user-input").value;
console.log("test")
if (comando === "AGENDAR") {
    console.log("HOLA")
  mostrarFormulario();
}
