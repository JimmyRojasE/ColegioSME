const formulario = document.querySelector('#matricula');
const rut = document.querySelector('input[name=rut]');
const region = document.querySelector('select[name=region]');
const comuna = document.querySelector('select[name=comuna]');
const toastcontroller = document.querySelector('.toast-message');

// rut.addEventListener('blur', async (ev) => {
//     if (ev.target.value.length < 2) return;

//     ev.target.value = ev.target.value.replace('-', '');
//     ev.target.value = ev.target.value.replace(/(\w)(\w)$/, '$1-$2').replace(/[.]/g, '');

//     const rut = ev.target.value.split('-')[0];
//     const dv = ev.target.value.split('-')[1];

//     showMessage('Buscando informacion de la persona...');

//     const request = await fetch(`http://190.161.35.216:8085/cl/csme/matriculas/api/obtener_persona/${rut}/${dv}`);
//     const response = await request.json();

//     if (response.length > 0) {
//         showMessage('Informacion encontrada.', 6000);

//         formatApiInfo(response);
//         Object.entries(response[0]).map(entry => {
//             const [key, value] = entry;
//             const input = formulario.querySelector(`input[name=${key}]`);

//             if (input !== null) {
//                 if (input.type === 'date') {
//                     input.value = value.split('T')[0];
//                 } else {
//                     input.value = value;
//                 }
//             }
//         });
//     } else {
//         showMessage('No se encontro informacion.', 6000);
//     }
// });
region.addEventListener('change', async (ev) => {
    console.log('Buen dia');

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

    const query = formulario.querySelectorAll('input, select');
    let body = {};

    for (let data of query) {
        body[data.name] = data.value;
    }
    body = format(body);
    showMessage('Verificando informacion, porfavor espere...');

    //REQUEST
    const request = await fetch('/crear-matricula-estudiante', {
        method: 'POST',
        headers: { 
            'Content-Type': 'application/json'
        },
        body: body
    });
    const response = await request.json();

    if (response['ok']) {
        showMessage('Informacion valida, redirigiendo...');
        console.log(response['id_matricula']);
        // setTimeout(() => {
        //     location.href = '/matricula-pdr'
        // }, 5000);
    } else {
        showMessage('Ocurrio un error, intentelo nuevamente.', 5000);
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
function formatApiInfo(data) {
    data = data[0];

    data['nombres'] = data['p_nombre'] + ' ' + data['s_nombre'];
    delete data['p_nombre'];
    delete data['s_nombre'];
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