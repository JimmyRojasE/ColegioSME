const formulario = document.querySelector('#matricula');
const rut = document.querySelector('input[name=rut]');
const region = document.querySelector('select[name=region]');
const comuna = document.querySelector('select[name=comuna]');
const toastcontroller = document.querySelector('.toast-message');

rut.addEventListener('blur', (ev) => {
    if (rut.value == '' || rut.length < 1) return;

    rut.value = rut.value.replace(/(\d)(\d)$/, '$1-$2').replace(/[.]/g, '');
});
region.addEventListener('change', async (ev) => {
    comuna.innerHTML = '<option value="" selected>Elija una opcion</option>';
    const request = await fetch('/static/environment/comunas.json');
    const comunas = await request.json();

    for (let i = 0; i < comunas[region.value].length; i++) {
        const data = comunas[region.value][i];
        comuna.innerHTML += `<option value="${data['id']}">${data['name']}</option>`;
    }
});
formulario.addEventListener('submit', async (ev) => {
    ev.preventDefault();

    const options = formulario.querySelectorAll('input, select');
    let data = {};
    for (let i = 0; i < options.length; i++) {
        const index = options[i];
        data[index.name] = index.value;
    }
    data = format(data);

    showMessage('Verificando informacion, porfavor espere.');

    const request = await fetch('http://190.161.35.216:8085/cl/csme/matriculas/api/matricula_alumno', { method: 'POST', body: data, headers: { 'Content-Type': 'application/json' } });
    const response = await request.json();

    if (response.ok) {
        showMessage('Informacion valida, redirigiendo...');
        setTimeout(() => {
            location.href = `/matricula-infoest/${response.data['id_matricula']}`;
        }, 4000);
    } else {
        showMessage('Hubo un error, intente nuevamente.', 5000);
    }
});

function format(data) {
    const nombres = data['nombres'].split(' ');
    data['p_nombre'] = nombres[0];
    data['s_nombre'] = nombres.slice(1).join(' ');
    delete data['nombres'];

    const rut = data['rut'].split('-');
    data['rut'] = rut[0];
    data['dv'] = rut[1];

    data['depto'] = data['depto'] == '' ? 0 : data['depto'];

    return JSON.stringify(data);
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