const formulario = document.querySelector('#form');
const run = formulario.querySelector('input[name=rut]');

run.addEventListener('blur', async (ev) => {
    if (ev.target.value.length < 2 || ev.target.value == '') return;

    // FORMAT RUN
    let run = ev.target.value.replace(/[^0-9kK]/g, '')
    ev.target.value = run.replace(/(\w)(\w)$/, '$1-$2');

    // GET INFO ABOUT PERSON
    const request = await fetch(`/getTeacherData/${run}`);
    const response = await request.json();

    
});