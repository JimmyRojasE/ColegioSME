const formulario = document.querySelector('#matricula');
const rut = document.querySelector('input[name=rut]');
const region = document.querySelector('select[name=region]');
const comuna = document.querySelector('select[name=comuna]');
const toastcontroller = document.querySelector('.toast-message');

rut.addEventListener('blur', async (ev) => {
    if (ev.target.value.length < 2 || ev.target.value === '') return;

    // FORMAT RUN
    let run = ev.target.value.replace(/[^0-9kK]/g, '')
    ev.target.value = run.replace(/(\w)(\w)$/, '$1-$2');

    // GET INFO ABOUT PERSON
    const request = await fetch(`/obtener-persona/${run}`);
    const response = await request.json();
    
    // FILL DATA IN FORM
    Object.entries(response).map(entry => {
        const [key, val] = entry;
        console.log({ key, val });

        const input = formulario.querySelector(`input[name=${key}]`);
        const select = formulario.querySelector(`select[name=${key}]`);


        if (input !== null) {
            input.value = val;
        }
        if (select !== null) {
            if (select.name === 'region') region.dispatchEvent(new Event('change'))
            select.value = val;
        }
    });
});
region.addEventListener('change', async (ev) => {
    comuna.innerHTML = '<option value="" selected>Elija una opcion</option>'

    const request = await fetch('/static/environment/comunas.json');
    const response = await request.json();

    const comunas = response[ev.target.value];
    for (let data of comunas) {
        comuna.innerHTML += `<option value="${data.id}">${data.name}</option>`;
    }
});
formulario.addEventListener('submit', async (ev) => {
    ev.preventDefault();

    const query = formulario.querySelectorAll('input, select');
    let body = {};

    for (let data of query) {
        body[data.name] = data.value;
    }
    body = format(body);
    
    const request = await fetch('/crear-matricula-estudiante', { headers: { 'Content-Type': 'application/json' }, method: 'POST', body: body});
    const response = await request.json();

    if (response.ok) {
        showMessage('Redirigiendo...');
        setTimeout(() => {
            location.href = `/matricula-infoest/${response.id_matricula}`
        }, 3000);
    }
});

function format(data) {
    data['rut'] = data['rut'].replace(/[^0-9kK]/g, '');

    data['p_nombre'] = data['nombres'].split(' ')[0];
    data['s_nombre'] = data['nombres'].split(' ').slice(1).join(' ');

    return JSON.stringify(data);
}
function formatResponse(data) {
    data['rut'] = `${data['run']}`.replace(/(\w)(\w)$/, '$1-$2');
    data['nombres'] = `${data['p_nombre']} ${data['s_nombre']}`;

    return data;
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