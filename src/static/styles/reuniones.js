const URL = '192.168.0.229:80';

function sendDelete(id) {
    fetch(`http://${ URL }/${ id }`, { method: 'DELETE' })
        .then(res => res.text())
        .then(res => window.location.reload())
        .catch(err => console.log(err))
}

try{
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
    fetch(`http://${ URL }/reuniones/${ id }`, config)
        .then(res => res.text())
        .then(res => window.location.href='/reuniones')
        .catch(err => console.log(err))
}