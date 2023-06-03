const formulario = document.querySelector('#matricula');
const toastcontroller = document.querySelector('.toast-message');
const matricula = document.currentScript.dataset;

window.onload = async () => {
    console.log(matricula);

    const request = await fetch(`/obtener-info-extra/${matricula.id}`);
    const response = await request.json()

    Object.entries(response).map(entry => {
        const [key, val] = entry;
        console.log({ key, val });

        const input = formulario.querySelector(`input[name=${key}]`);
        const select = formulario.querySelector(`select[name=${key}]`);

        if (input !== null) {
            if (input.type === 'radio') {
                if (key === 'pie' && !val) alternarAutorizaEvaluacion(true);

                const checkbox = formulario.querySelector(`input[name=${key}][value=${val}]`);
                checkbox.checked = true;
            }
            input.value = val;
        }
        if (select !== null) {
            select.value = val;
        }
    });
};
 
formulario.addEventListener('submit', async (ev) => {
    ev.preventDefault();

    const options = formulario.querySelectorAll('input');
    let data = {}
    for (let i = 0; i < options.length; i++) {
        const index = options[i];
        if (index.type == 'radio') {
            if (index.checked) {
                data[index.name] = index.value;
            }
        } else {
            data[index.name] = index.value;
        }
    }

    showMessage('Verificando informacion, porfavor espere.');

    const request = await fetch(`http://190.161.35.216:8085/cl/csme/matriculas/api/info_alumno/${matricula.id}`, { method: 'PUT', body: JSON.stringify(data), headers: { 'Content-Type': 'application/json' } });
    const response = await request.json();

    if (response.ok) {
        showMessage('Informacion valida, redirigiendo...');
        setTimeout(() => {
            location.href = `/matricula-pdr/${matricula.id}`;
        }, 4000);
    } else {
        showMessage('Hubo un error, intente nuevamente.', 5000);
    }
});

function alternarEtnia(mostrar) {
    const option = mostrar ? 'block' : 'none';
    const etnia = document.querySelector('#indiqueEtnia');

    etnia.style.display = option;
}
function alternarAutorizaEvaluacion(mostrar) {
    const option = mostrar ? 'block' : 'none';
    const autorizaEvaluacion = document.querySelector('#autorizaEvaluacion');

    autorizaEvaluacion.style.display = option;
}

function showMessage(message, duration = 0) {
    toastcontroller.style.display = 'block';
    toastcontroller.innerHTML = message;

    if (duration > 0) {
        setTimeout(() => {
            toastcontroller.style.display = 'none';
            toastcontroller.innerHTML = '';
        }, duration);
    }
}