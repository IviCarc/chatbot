// Obtener el elemento del calendario
const calendario = document.getElementById('calendario');

// Crear una función para generar el calendario
function generarCalendario() {
  // Lógica para generar el calendario
}

// Llamar a la función para generar el calendario
generarCalendario();

function generarCalendario() {
    // Lógica para generar el calendario
  
    // Obtener la fecha actual
    const fechaActual = new Date();
  
    // Iterar sobre cada día del calendario
    for (let dia of diasCalendario) {
      // Bloquear las fechas no disponibles
      if (!esFechaDisponible(dia)) {
        dia.classList.add('no-disponible');
      }
  
      // Limitar el horario a solo entre las 14hs y las 15hs
      if (dia.classList.contains('disponible')) {
        const horas = dia.getElementsByClassName('hora');
        for (let hora of horas) {
          if (hora.value < 14 || hora.value >= 15) {
            hora.disabled = true;
          }
        }
      }
    }
  }
  
  // Función para verificar si una fecha está disponible
  function esFechaDisponible(dia) {
    // Lógica para determinar si la fecha está disponible
  }
  
  // Llamar a la función para generar el calendario
  generarCalendario();
  