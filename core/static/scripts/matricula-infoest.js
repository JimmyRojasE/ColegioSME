const form = document.getElementById('matricula');
const id = new URLSearchParams(window.location.search).get('id');

if (id == null) {
    alert('No se detecto id de matricula, redirigiendo al registro.');
    location.href = '/matricula-est'
}

console.log(id);

form.addEventListener('submit', async (ev) => {
    ev.preventDefault();

    const inputs = form.querySelectorAll('input');
    let data = {};
    for (let i = 0; i < inputs.length; i++) {
        const input = inputs[i];

        if (input.type == 'radio') {
            if (input.checked) {
                data[input.name] = input.value;
            }
        } else {
            data[input.name] = input.value || "";
        }
    }

    fetch(`http://190.161.35.216:3000/cl/csme/matriculas/api/info_alumno/${id_matricula}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'  
        },
        body: JSON.stringify(data)
    })
    .then(data => data.json())
    .then(response => {
        console.log(response);
    })
    .catch(err => {
        console.log(err);
    })
});