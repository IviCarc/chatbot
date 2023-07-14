const validateInput = (input) => {
    const regex = {
        nombre : /^[A-Za-z]{3,}$/,
        asunto : /^[A-Za-z]{1,}/,
        fechaHora : /^\d{2}\/\d{2}\/\d{4} \d{2}:\d{2}:\d{2}$/,
        correo : /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
    }

    if (regex[input.name].test(input.value)) {
        input.classList.add('is-valid');
        input.classList.remove('is-invalid');
    } else {
        input.classList.add('is-invalid');
        input.classList.remove('is-valid');
    }
}
