const formulario = document.querySelector('form');
const region = document.querySelectorAll('select[name=region]');
const comuna = document.querySelectorAll('select[name=comuna]');
const rut = document.querySelectorAll('input[name=rut]');
const matricula = document.currentScript.dataset;

rut[0].addEventListener('blur', (ev) => {
    if (rut[0].value == '' || rut[0].length < 1) return;

    rut[0].value = rut[0].value.replace(/(\d)(\d)$/, '$1-$2').replace(/[.]/g, '');
});
rut[1].addEventListener('blur', (ev) => {
    if (rut[1].value == '' || rut[1].length < 1) return;

    rut[1].value = rut[1].value.replace(/(\d)(\d)$/, '$1-$2').replace(/[.]/g, '');
});

region[0].addEventListener('change', async (ev) => {
    comuna[0].innerHTML = '<option value="" selected>Elija una opcion</option>';
    const request = await fetch('/static/environment/comunas.json');
    const comunas = await request.json();

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

formulario.addEventListener('submit', async (ev) => {
    ev.preventDefault();
    const fieldsets = formulario.querySelectorAll('fieldset');
    let data = { principal: {}, suplente: {} };

    const principal = fieldsets[0].querySelectorAll('input, select');
    const suplente = fieldsets[1].querySelectorAll('input, select');

    for (let i = 0; i < principal.length; i++) {
        const index = principal[i];
        if (index.type == 'radio') {
            if (index.checked) {
                data.principal[index.name] = index.value;
            }
        } else {
            data.principal[index.name] = index.value;
        }
    }
    for (let i = 0; i < suplente.length; i++) {
        const index = suplente[i];
        if (index.type == 'radio') {
            if (index.checked) {
                data.suplente[index.name] = index.value;
            }
        } else {
            data.suplente[index.name] = index.value;
        }
    }

    console.log(data);
});


// const form = document.querySelector('form');
// const region = document.querySelectorAll('select[name=region]');
// const comuna = document.querySelectorAll('select[name=comuna]');
// const rut = document.querySelectorAll('input[name=rut]');
// const matricula = document.currentScript.dataset;

// rut[0].addEventListener('blur', async (ev) => {
//     if (rut[0].value == '') {
//         return;
//     }

//     const formatted = formatRut(rut[0].value)
//     rut[0].value = formatted;
// });
// rut[1].addEventListener('blur', async (ev) => {
//     if (rut[1].value == '') {
//         return;
//     }

//     const formatted = formatRut(rut[1].value)
//     rut[1].value = formatted;
// });

// region[0].addEventListener('change', async (ev) => {
//     if (region[0].value == '') {
//         comuna[0].innerHTML = '<option value="" selected>Elija una opcion</option>';
//     }

//     const data = comunas[region[0].value];
//     let string = `<option value="" selected>Elija una opcion</option>`;
//     data.forEach(x => string += `<option value="${x.id}">${x.name}</option>`);

//     comuna[0].innerHTML = string;
// });
// region[1].addEventListener('change', async (ev) => {
//     if (region[1].value == '') {
//         comuna[1].innerHTML = '<option value="" selected>Elija una opcion</option>';
//     }

//     const data = comunas[region[1].value];
//     let string = `<option value="" selected>Elija una opcion</option>`;
//     data.forEach(x => string += `<option value="${x.id}">${x.name}</option>`);

//     comuna[1].innerHTML = string;
// });

// form.addEventListener('submit', async (ev) => {
//     ev.preventDefault();

//     const fieldsets = form.querySelectorAll('fieldset');
//     let data = {
//         principal: {},
//         suplente: {}
//     }

//     const dataPrincipal = fieldsets[0].querySelectorAll('input, select');
//     const dataSuplente = fieldsets[1].querySelectorAll('input, select');

//     for (let i = 0; i < dataPrincipal.length; i++) {
//         const input = dataPrincipal[i];

//         if (input.type == 'radio') {
//             if (input.checked) {
//                 data.principal[input.name] = input.value;
//             }
//         } else {
//             data.principal[input.name] = input.value;
//         }
//     }
//     for (let i = 0; i < dataSuplente.length; i++) {
//         const input = dataSuplente[i];

//         if (input.type == 'radio') {
//             if (input.checked) {
//                 data.suplente[input.name] = input.value;
//             }
//         } else {
//             data.suplente[input.name] = input.value;
//         }
//     }

//     const request = await fetch(`http://190.161.35.216:8085/cl/csme/matriculas/api/matricula_apoderado/${matricula.id}`, { method: 'POST', body: JSON.stringify(data), headers: { 'Content-Type': 'application/json' } });
//     const response = await request.json();

//     if (response.ok) {
//         console.log('OK');
//     } else {
//         console.log('ERROR');
//     }
// });

// function mostrarDireccionApd() {
//     var direccionApd = document.getElementById("direccionApd");
//     direccionApd.style.display = "block";
// }
// function ocultarDireccionApd() {
//     var direccionApd = document.getElementById("direccionApd");
//     direccionApd.style.display = "none";
// }

// function mostrarDireccionSup() {
//     var direccionSup = document.getElementById('direccionSup');
//     direccionSup.style.display = "block";
// }
// function ocultarDireccionSup() {
//     var direccionSup = document.getElementById('direccionSup');
//     direccionSup.style.display = "none";
// }

// function formatRut(rut) {
//     if (rut == '') {
//         return '';
//     }

//     rut = rut.toString();
//     var sRut = (rut + '').replace(/[^\dkK]/g, '');
//     var sRutDV = sRut.slice(-1);
//     sRut = sRut.slice(0, -1);
//     var sFormatted = '';
//     while (sRut.length > 3) {
//         sFormatted = '.' + sRut.slice(-3) + sFormatted;
//         sRut = sRut.slice(0, -3);
//     }
//     sFormatted = sRut + sFormatted;
//     sFormatted += '-' + sRutDV;
//     return sFormatted;
// }