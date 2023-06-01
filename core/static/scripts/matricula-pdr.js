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
    const padre = formulario[0].querySelectorAll('input, select');
    const madre = formulario[1].querySelectorAll('input, select');
    let data = {
        padre: {},
        madre: {}
    };

    for (let i = 0; i < padre.length; i++) {
        if (padre[i].type === 'radio') {
            if (padre[i].checked) {
                data.padre[padre[i].name] = padre[i].value;
            }
        } else {
            data.padre[padre[i].name] = padre[i].value;
        }
    }
    for (let i = 0; i < madre.length; i++) {
        if (madre[i].type === 'radio') {
            if (madre[i].checked) {
                data.madre[madre[i].name] = madre[i].value;
            }
        } else {
            data.madre[madre[i].name] = madre[i].value;
        }
    }
    format(data);
    showMessage('Verificando informacion, porfavor espere.');

    const request = await fetch(`http://190.161.35.216:8085/cl/csme/matriculas/api/matricula_padres/${matricula.id}`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
    const response = await request.json();

    if (response.ok) {
        showMessage('Informacion valida, redirigiendo...');
        setTimeout(() => {
            location.href = `/matricula-apd/${matricula.id}`;
        }, 4000);
    } else {
        showMessage('Hubo un error, intente nuevamente.', 5000);
    }
});

function format(obj) {
    //PADRE
    const rut_padre = obj.padre['rut'].split('-');
    obj.padre['rut'] = rut_padre[0];
    obj.padre['dv'] = rut_padre[1];

    const nombres_padre = obj.padre['nombres'].split(' ');
    obj.padre['p_nombre'] = nombres_padre[0];
    obj.padre['s_nombre'] = nombres_padre.slice(1).join(' ');
    delete obj.padre['nombres'];

    obj.padre['vive_con_alumno'] = (obj.padre['vive_con_alumno'] === 'true');

    //MADRE
    const rut_madre = obj.madre['rut'].split('-');
    obj.madre['rut'] = rut_madre[0];
    obj.madre['dv'] = rut_madre[1];

    const nombres_madre = obj.madre['nombres'].split(' ');
    obj.madre['p_nombre'] = nombres_madre[0];
    obj.madre['s_nombre'] = nombres_madre.slice(1).join(' ');
    delete obj.madre['nombres'];

    obj.madre['vive_con_alumno'] = (obj.madre['vive_con_alumno'] === 'true');
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