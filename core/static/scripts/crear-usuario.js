const form = document.getElementById('crear-usuario');
const run = document.querySelector('input[name=run]');

const region = document.querySelector('select[name=region]');
const comuna = document.querySelector('select[name=comuna]');
let comunas = {};

const toast = document.querySelector('.toast-message');
toast.style.display = 'none';

let form_type = 'Create';

fetch('/static/scripts/comunas.json').then(data => data.json()).then(response => comunas = response).catch(err => console.log(err));

run.addEventListener('blur', (ev) => {
    const formatted = formatRut(run.value)
    run.value = formatted;

    const searched = formatted.split('-').slice(0, 1)[0].split('.').join('');
    const dv = formatted.split('-')[1];
})

form.addEventListener('submit', async (ev) => {
    ev.preventDefault();

    const inputs = document.querySelectorAll('input');
    const options = document.querySelectorAll('select');
    const button = document.querySelector('button[type=submit]');
    let data = {};

    for (let i = 0; i < inputs.length; i++) {
        const input = inputs[i];

        if (input.type == 'radio') {
            if (input.checked) {
                data[input.name] = input.value;
            }
        } else {
            data[input.name] = input.value;
        }
    }
    for (let i = 0; i < options.length; i++) {
        const option = options[i];
        data[option.name] = option.value;
    }

    button.disabled = true;
    toast.style.display = 'block';
    toast.innerHTML = 'Guardando informacion, por favor espere...';

    if (form_type == 'Create') {
        fetch('http://190.161.35.216:8085/cl/csme/usuarios/api/crear_usuario', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(data => data.json())
            .then(response => {
                console.log(response);
                    if (response.ok) {
                        toast.innerHTML = 'Informacion guardada con exito, redirigiendo...';
                        setTimeout(() => {
                            location.href = `/matricula-infoest/${id_matricula}`;
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
                console.log(err);

                toast.innerHTML = 'Hubo un error interno, intente nuevamente...';
                button.disabled = false;

                setTimeout(() => {
                    toast.style.display = 'none';
                }, 4000)
            });
    } else if (form_type == 'Modify') {
        fetch('')
            .then()
            .then()
            .catch();
    }
});

function mostrarCargo() {
    var cargoAdmin = document.getElementById("cargoAdmin");
    cargoAdmin.style.display = "block";
}

function ocultarCargo() {
    var cargoAdmin = document.getElementById("cargoAdmin");
    cargoAdmin.style.display = "none";
}

function formatRut(rut) {
    if (rut == '') {
        return '';
    }

    rut = rut.toString();
    var sRut = (rut + '').replace(/[^\dkK]/g, '');
    var sRutDV = sRut.slice(-1);
    sRut = sRut.slice(0, -1);
    var sFormatted = '';
    while (sRut.length > 3) {
        sFormatted = '.' + sRut.slice(-3) + sFormatted;
        sRut = sRut.slice(0, -3);
    }
    sFormatted = sRut + sFormatted;
    sFormatted += '-' + sRutDV;
    return sFormatted;
}

region.addEventListener('change', (ev) => {
    if (region.value === '') {
        comuna.innerHTML = '<option value="" selected>Elija una opción</option>';
        return;
    }

    const data = comunas[region.value];
    let string = '';
    for (let i = 0; i < data.length; i++) {
        string += `<option value="${data[i].id}">${data[i].name}</option>`
    }
    comuna.innerHTML = string;
});