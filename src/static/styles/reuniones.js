function sendDelete(id) {
    fetch("http://localhost:80/" + id, { method: 'DELETE' })
        .then(res => res.text())
        .then(res => window.location.reload())
        .catch(err => console.log(err))
}

// if (window.location.href == 'http://localhost:80/reuniones/') {
// }
try {
    document.getElementById("form").addEventListener("submit", (e) => {
        e.preventDefault()
    });
} catch {
}

sendUpdate = (id) => {
    let formData = new FormData(document.getElementById("form"));
    // console.log(Object.fromEntries(formData), id)
    let config = {
        method: 'PUT',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(Object.fromEntries(formData))
    }
    fetch("http://localhost:80/reuniones/" + id, config)
        .then(res => res.text())
        .then(res => window.location.href = '/reuniones')
        .catch(err => console.log(err))
}