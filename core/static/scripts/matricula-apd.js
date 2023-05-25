const formulario = document.querySelectorAll('form');
const rut = document.querySelectorAll('input[name="rut"]');
const region = document.querySelectorAll('select[name="region"]');
const comuna = document.querySelectorAll('select[name="comuna"]');
const toastcontroller = document.querySelector('.toast-message');
const matricula = document.currentScript.dataset;

rut[0].addEventListener('blur', (ev) => {
    if (ev.target.value.length < 2) return;

    ev.target.value = ev.target.value.replace('-', '');
    ev.target.value = ev.target.value.replace(/(\w)(\w)$/, '$1-$2').replace(/[.]/g, '');
});
rut[1].addEventListener('blur', (ev) => {
    if (ev.target.value.length < 2) return;

    ev.target.value = ev.target.value.replace('-', '');
    ev.target.value = ev.target.value.replace(/(\w)(\w)$/, '$1-$2').replace(/[.]/g, '');
});
region[0].addEventListener('change', async (ev) => {
    const request = await fetch('/static/environment/comunas.json');
    const comunas = await request.json();

    comuna[0].innerHTML = '<option value="" selected>Elija una opción</option>';
    for (let i = 0; i < comunas[ev.target.value].length; i++) {
        const data = comunas[ev.target.value][i];
        comuna[0].innerHTML += `<option value="${data.id}">${data.name}</option>`;
    }
});
region[1].addEventListener('change', async (ev) => {
    const request = await fetch('/static/environment/comunas.json');
    const comunas = await request.json();

    comuna[1].innerHTML = '<option value="" selected>Elija una opción</option>';
    for (let i = 0; i < comunas[ev.target.value].length; i++) {
        const data = comunas[ev.target.value][i];
        comuna[1].innerHTML += `<option value="${data.id}">${data.name}</option>`;
    }
});

formulario[1].addEventListener('submit', async (ev) => {
    ev.preventDefault();
    const principal = formulario[0].querySelectorAll('input, select');
    const suplente = formulario[1].querySelectorAll('input, select');
    let data = {
        principal: {},
        suplente: {}
    };

    for (let i = 0; i < principal.length; i++) {
        if (principal[i].type === 'radio') {
            if (principal[i].checked) {
                data.principal[principal[i].name] = principal[i].value;
            }
        } else {
            data.principal[principal[i].name] = principal[i].value;
        }
    }
    for (let i = 0; i < suplente.length; i++) {
        if (suplente[i].type === 'radio') {
            if (suplente[i].checked) {
                data.suplente[suplente[i].name] = suplente[i].value;
            }
        } else {
            data.suplente[suplente[i].name] = suplente[i].value;
        }
    }
    format(data);
    showMessage('Verificando informacion, porfavor espere.');

    const request = await fetch(`http://190.161.35.216:8085/cl/csme/matriculas/api/matricula_apoderado/${matricula.id}`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
    const response = await request.json();

    if (response.ok) {
        showMessage('Informacion valida, gracias por matricular.');
    } else {
        showMessage('Hubo un error, intente nuevamente.', 5000);
    }
});

function format(obj) {
    //principal
    const rut_principal = obj.principal['rut'].split('-');
    obj.principal['rut'] = rut_principal[0];
    obj.principal['dv'] = rut_principal[1];

    const nombres_principal = obj.principal['nombres'].split(' ');
    obj.principal['p_nombre'] = nombres_principal[0];
    obj.principal['s_nombre'] = nombres_principal.slice(1).join(' ');
    delete obj.principal['nombres'];

    obj.principal['vive_con_alumno'] = (obj.principal['vive_con_alumno'] === 'true');

    //suplente
    const rut_suplente = obj.suplente['rut'].split('-');
    obj.suplente['rut'] = rut_suplente[0];
    obj.suplente['dv'] = rut_suplente[1];

    const nombres_suplente = obj.suplente['nombres'].split(' ');
    obj.suplente['p_nombre'] = nombres_suplente[0];
    obj.suplente['s_nombre'] = nombres_suplente.slice(1).join(' ');
    delete obj.suplente['nombres'];

    obj.suplente['vive_con_alumno'] = (obj.suplente['vive_con_alumno'] === 'true');
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

function alternarDireccionPdr(bool) {
    const direccion = formulario[0].querySelector('.hidden');
    const option = bool ? 'block' : 'none';

    direccion.style.display = option;
}

function alternarDireccionMdr(bool) {
    const direccion = formulario[1].querySelector('.hidden');
    const option = bool ? 'block' : 'none';

    direccion.style.display = option;
}