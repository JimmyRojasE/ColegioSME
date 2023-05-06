const form = document.getElementById('matricula');
const matricula = document.currentScript.dataset;

const toast = document.querySelector('.toast-message');
toast.style.display = 'none';

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

    toast.style.display = 'block';
    toast.innerHTML = 'Modificando informacion, por favor espere...';

    fetch(`http://190.161.35.216:8085/cl/csme/matriculas/api/info_alumno/${matricula.id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'  
        },
        body: JSON.stringify(data)
    })
    .then(data => data.json())
    .then(response => {
        if (response.ok) {
            toast.innerHTML = 'Informacion guardada con exito, redirigiendo...';

            setTimeout(() => {
                location.href = `/matricula-pdr/${matricula.id}`;
                toast.style.display = 'none';
            }, 6000)
        } else {
            toast.innerHTML = 'Se encontro un error, revise la informacion e ingrese nuevamente.';

            setTimeout(() => {
                toast.style.display = 'none';
            }, 4000)
        }
    })
    .catch(err => {
        toast.innerHTML = 'Hubo un error interno, intente nuevamente...';
        setTimeout(() => {
            toast.style.display = 'none';
        }, 4000)
    })
});