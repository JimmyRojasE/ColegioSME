const form = document.querySelector('#matricula');
const rut = document.querySelectorAll('input[name=rut]');
const region = document.querySelectorAll('select[name=region]');
const comuna = document.querySelectorAll('select[name=comuna]');
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
    data = format(data);

    const request = await fetch(`http://190.161.35.216:8085/cl/csme/matriculas/api/matricula_padres/${matricula.id}`, { method: 'POST', body: JSON.stringify(data), headers: { 'Content-Type': 'application/json' } });
    const response = await request.json();

    if (response.ok) {
        location.href = `/matricula-apd/${matricula.id}`;
    } else {
        console.log('A ocurrido un error.');
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
    delete data.padres['nombres'];

    const nombres1 = data.madres['nombres'].split(' ');
    data.madres['p_nombre'] = nombres1[0];
    data.madres['s_nombre'] = nombres1.slice(1).join(' ');
    delete data.madres['nombres'];

    const rut = data.padre['rut'].split('-');
    data.padre['rut'] = rut[0];
    data.padre['dv'] = rut[1];

    const rut1 = data.madre['rut'].split('-');
    data.madre['rut'] = rut1[0];
    data.madre['dv'] = rut1[1];

    data.padre['depto'] = data.padre['depto'] == '' ? 0 : data.padre['depto'];
    data.madre['depto'] = data.madre['depto'] == '' ? 0 : data.madre['depto'];

    return JSON.stringify(data);
}

// const form = document.querySelector('form');
// const madreRegion = document.querySelector('#direccionMdr > div:nth-child(2) > div:nth-child(1) > select');
// const padreRegion = document.querySelector('#direccionPdr > div:nth-child(2) > div:nth-child(1) > select');
// const padreComuna = document.querySelector('#direccionPdr > div:nth-child(2) > div:nth-child(2) > select');
// const madreComuna = document.querySelector('#direccionMdr > div:nth-child(2) > div:nth-child(2) > select');
// const matricula = document.currentScript.dataset;

// console.log(matricula.id);

// let datosPadre = true;
// let datosMadre = true;

// form.addEventListener('submit', async (ev) => {
//     ev.preventDefault();

//     const fieldsets = form.querySelectorAll('fieldset');
//     let data = {
//         padre: {},
//         madre: {}
//     }
//     if (datosPadre) {
//         const padreInfo = fieldsets[0].querySelectorAll('input');
//         const padreInfoSelects = fieldsets[0].querySelectorAll('select');

//         for (let i = 0; i < padreInfo.length; i++) {
//             const info = padreInfo[i];
            
//             if (info.type == 'radio') {
//                 if (info.checked) {
//                     data.padre[info.name] = info.value;
//                 }
//             } else {
//                 data.padre[info.name] = info.value;
//             }
//         }
//         for (let i = 0; i < padreInfoSelects.length; i++) {
//             const info = padreInfoSelects[i];
//             data.padre[info.name] = info.value;
//         }
//     } else {
//         delete data['padre'];
//     }

//     if (datosMadre) {
//         const madreInfo = fieldsets[1].querySelectorAll('input');
//         const madreInfoSelects = fieldsets[1].querySelectorAll('select');

//         for (let i = 0; i < madreInfo.length; i++) {
//             const info = madreInfo[i];

//             if (info.type == 'radio') {
//                 if (info.checked) {
//                     data.madre[info.name] = info.value;
//                 }
//             } else {
//                 data.madre[info.name] = info.value;
//             }
//         }
//         for (let i = 0; i < madreInfoSelects.length; i++) {
//             const info = madreInfoSelects[i];
//             data.madre[info.name] = info.value;
//         }
//     } else {
//         delete data['madre'];
//     }

//     fetch(`http://190.161.35.216:8085/cl/csme/matriculas/api/matricula_padres/${matricula.id}`, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(data)
//     })
//     .then(data => data.json())
//     .then(response => {
//         console.log(response);
//     })
//     .catch(err => {
//         console.log(err);
//     })
// });

// function ocultarDatosMadre() {
//     var div = document.getElementById("datosMadre");
//     var checkbox = document.getElementById("chboxOcultarDatosMadre");

//     if (checkbox.checked) {
//         div.style.display = "none";
//         datosMadre = false;
//     } else {
//         div.style.display = "block";
//         datosMadre = true;
//     }
// }
// function ocultarDatosPadre() {
//     var div = document.getElementById("datosPadre");
//     var checkbox = document.getElementById("chboxOcultarDatosPadre");

//     if (checkbox.checked) {
//         div.style.display = "none";
//         datosPadre = false;
//     } else {
//         div.style.display = "block";
//         datosPadre = true;
//     }
    
// }

// function mostrarDireccionMdr() {
//     var direccionMdr = document.getElementById("direccionMdr");
//     direccionMdr.style.display = "block";
// }
// function ocultarDireccionMdr() {
//     var direccionMdr = document.getElementById("direccionMdr");
//     direccionMdr.style.display = "none";
// }
// function mostrarDireccionPdr() {
//     var direccionPdr = document.getElementById('direccionPdr');
//     direccionPdr.style.display = "block";
// }
// function ocultarDireccionPdr() {
//     var direccionPdr = document.getElementById('direccionPdr');
//     direccionPdr.style.display = "none";
// }