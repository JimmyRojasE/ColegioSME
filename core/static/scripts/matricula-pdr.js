const form = document.querySelector('#matricula');
const rut = document.querySelectorAll('input[name=rut]');
const region = document.querySelectorAll('select[name=region]');
const comuna = document.querySelectorAll('select[name=comuna]');
const toastcontroller = document.querySelector('.toast-message');
const matricula = document.currentScript.dataset;

rut[0].addEventListener('blur', (ev) => {
    if (rut[0].value == '' || rut[0].length < 1) return;

    rut[0].value = rut[0].value.replace(/(\d)(\d)$/, '$1-$2').replace(/[.]/g, '');;
});
rut[1].addEventListener('blur', (ev) => {
    if (rut[1].value == '' || rut[1].length < 1) return;

    rut[1].value = rut[1].value.replace(/(\d)(\d)$/, '$1-$2').replace(/[.]/g, '');;
});
region[0].addEventListener('change', async (ev) => {
    comuna[0].innerHTML = '<option value="" selected>Elija una opcion</option>';
    const request = await fetch('/static/environment/comunas.json');
    const comunas = await request.json();

    console.log(comunas[region[0].value]);

    for (let i = 0; i < comunas[region[0].value].length; i++) {
        const data = comunas[region[0].value][i];
        comuna[0].innerHTML += `<option value="${data['id']}">${data['name']}</option>`;
    }
});
region[1].addEventListener('change', async (ev) => {
    comuna[1].innerHTML = '<option value="" selected>Elija una opcion</option>';
    const request = await fetch('/static/environment/comunas.json');
    const comunas = await request.json();

    for (let i = 0; i < comunas[region[1].value].length; i++) {
        const data = comunas[region[1].value][i];
        comuna[1].innerHTML += `<option value="${data['id']}">${data['name']}</option>`;
    }
});

form.addEventListener('submit', async (ev) => {
    ev.preventDefault();

    const fieldsets = document.querySelectorAll('fieldset');
    let data = { padre: {}, madre: {} }

    const padre = fieldsets[0].querySelectorAll('input, select');
    const madre = fieldsets[1].querySelectorAll('input, select');

    for (let i = 0; i < padre.length; i++) {
        const index = padre[i];
        if (index.type == 'radio') {
            if (index.checked) {
                data.padre[index.name] = index.value;
            }
        } else {
            data.padre[index.name] = index.value;
        }
    }
    for (let i = 0; i < madre.length; i++) {
        const index = madre[i];
        if (index.type == 'radio') {
            if (index.checked) {
                data.madre[index.name] = index.value;
            }
        } else {
            data.madre[index.name] = index.value;
        }
    }
    format(data);

    showMessage('Verificando informacion, porfavor espere.');

    const request = await fetch(`http://190.161.35.216:8085/cl/csme/matriculas/api/matricula_padres/${matricula.id}`, { method: 'POST', body: JSON.stringify(data), headers: { 'Content-Type': 'application/json' } });
    const response = await request.json();

    if (response.ok) {
        showMessage('Informacion valida, redirigiendo...');
        setTimeout(() => {
            location.href = `/matricula-apd/${matricula.id}`;
        }, 4000)
    } else {
        showMessage('Hubo un error, intente nuevamente.', 5000);
    }
});

function alternarDireccionPdr(mostrar) {
    const option = mostrar ? 'block' : 'none';
    const direccionPdr = document.querySelector('#direccionPdr');

    direccionPdr.style.display = option;
}
function alternarDireccionMdr(mostrar) {
    const option = mostrar ? 'block' : 'none';
    const direccionMdr = document.querySelector('#direccionMdr');

    direccionMdr.style.display = option;
}

function format(data) {
    const nombres = data.padre['nombres'].split(' ');
    data.padre['p_nombre'] = nombres[0];
    data.padre['s_nombre'] = nombres.slice(1).join(' ');
    delete data.padre['nombres'];

    const nombres1 = data.madre['nombres'].split(' ');
    data.madre['p_nombre'] = nombres1[0];
    data.madre['s_nombre'] = nombres1.slice(1).join(' ');
    delete data.madre['nombres'];

    const rut = data.padre['rut'].split('-');
    data.padre['rut'] = rut[0];
    data.padre['dv'] = rut[1];

    const rut1 = data.madre['rut'].split('-');
    data.madre['rut'] = rut1[0];
    data.madre['dv'] = rut1[1];

    data.padre['depto'] = data.padre['depto'] == '' ? 0 : data.padre['depto'];
    data.madre['depto'] = data.madre['depto'] == '' ? 0 : data.madre['depto'];
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