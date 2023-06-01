from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from .serializers import *
from .models import *
from .forms import *
import json

# Create your views here readonly.
def inicio(request):
    return render(request, 'index.html')

def matriculasEst(request):
    return render(request, 'matricula/matricula-est.html')

def matriculasInfoest(request, id):
    return render(request, 'matricula/matricula-infoest.html', { 'id_matricula': id })

def matriculasPdr(request, id):
    return render(request, 'matricula/matricula-pdr.html', { 'id_matricula': id })

def matriculasApd(request, id):
    return render(request, 'matricula/matricula-apd.html', { 'id_matricula': id })

def login (request):
    if request.method=='POST':
        try:
            usuario = Usuario.objects.get(id_usuario=request.POST['id_usuario'], password=request.POST['password'])
            persona = Persona.objects.get(run=request.POST['id_usuario'])
            request.session['nombre'] = f'{persona.p_nombre} {persona.app_paterno}'

            return render(request, 'index.html')
        except Usuario.DoesNotExist as e:
            messages.success(request, 'Usuario o contraseña incorrectos...')
        except Persona.DoesNotExist as e:
            messages.success(request, 'Falta Ingresar Datos Personales...')
        except:
            messages.success(request, 'Ingrese Información Válida...')

    return render(request, 'auth/login.html', { 'form': UsuarioForm() })

def logout(request):
    del request.session['nombre']
    return render(request, 'index.html')

def crearProfesor(request):
    return render(request, 'profesor/crear-profesor.html')

def listarCurso(request):
    cursos = Curso.objects.all()

    return render(request, 'curso/listar-cursos.html', { 'cursos': cursos })

def crearCurso(request):
    data = {
        'form': CursoForm()
    }

    if request.method == 'POST':
        formulario = CursoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarCurso")
        else:
            data["form"] = formulario

    return render(request, 'curso/crear-curso.html', data)

def editarCurso(request, id):
    curso = get_object_or_404(Curso, id_curso=id)
    data = {
        'form': CursoForm(instance=curso)
    }

    if request.method == 'POST':
        formulario = CursoForm(data=request.POST, instance=curso)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarCurso")
        data['form'] = formulario

    return render(request, 'curso/editar-curso.html', data)

def eliminarCurso(request, id):
    curso = get_object_or_404(Curso, id_curso=id)
    curso.delete()
    return redirect(to="listarCurso")

def listarColegio(request):
    colegios = Colegio.objects.all()
    return render(request, 'colegio/listar-colegio.html', { 'cursos': colegios })

def crearColegio(request):
    data = {
        'form':ColegioForm(),
        'form2':DireccionForm()
    }

    if request.method == 'POST':
        formulario = ColegioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarColegio")
        else:
            data["form"] = formulario

    return render(request, 'colegio/crear-colegio.html', data)

def editarColegio(request, id):
    colegio = get_object_or_404(Colegio, id_colegio=id)
    data = {
        'form': ColegioForm(instance=colegio)
    }

    if request.method == 'POST':
        formulario = ColegioForm(data=request.POST,instance=colegio)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarColegio")
        data['form'] = formulario

    return render(request, 'colegio/editar-colegio.html', data)

def eliminarColegio(request, id):
    curso = get_object_or_404(Colegio, id_colegio=id)
    curso.delete()
    return redirect(to="listarColegio")

def listarGrupoFamiliar(request, id):
    grupoFamiliar = GrupoFamiliar.objects.filter(id_matricula=id)
    data = {
        'grupoFamiliar': grupoFamiliar,
        'id_matricula': id
    }

    return render(request, 'grupoFamiliar/listar-grupoFamiliar.html', data)

def crearGrupoFamiliar(request, id):
    data = {
        'form': GrupoFamiliarForm(initial= { 'id_matricula': id } ),
        'id_matricula': id
    }

    if request.method == 'POST':
        formulario = GrupoFamiliarForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to=f"/listar-grupoFamiliar/{id}")
        else:
            data["form"] = formulario

    return render(request, 'grupoFamiliar/crear-grupoFamiliar.html', data)

def editarGrupoFamiliar(request, id, id_matricula):
    grupofamiliar = get_object_or_404(GrupoFamiliar,id_gr_fam=id)
    data = {
        'form': GrupoFamiliarForm(instance=grupofamiliar)
    }

    if request.method == 'POST':
        formulario = GrupoFamiliarForm(data=request.POST,instance=grupofamiliar)
        if formulario.is_valid():
            formulario.save()
            return redirect(to=f"/listar-grupoFamiliar/{id_matricula}")
        data['form'] = formulario

    return render(request, 'grupoFamiliar/editar-grupoFamiliar.html', data)

def eliminarGrupoFamiliar(request, id, id_matricula):
    curso = get_object_or_404(GrupoFamiliar, id_gr_fam=id)
    curso.delete()
    return redirect(to=f"listarGrupoFamiliar/{id_matricula}")

def crearUsuario(request):
    return render(request, 'usuarios/crear-usuario.html')

def listarUsuario(request):
    personas = Persona.objects.all()
    return render(request,'usuarios/listar-usuario.html', {'personas': personas })

def editarUsuario(request):
    return render(request,'usuarios/editar-usuario.html')

def eliminarUsuario(request, id):
    usuario = Usuario.objects.get(id_usuario=id)
    usuario.delete()
    return redirect(to="listarUsuario")

def crearCursoReprobado(request):
    data = {
        'form': CursoRepetidoForm()
    }

    if request.method == 'POST':
        formulario = CursoRepetidoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarCursoRepetido")
        else:
            data["form"] = formulario

    return render(request, 'cursosReprobados/crear-curso-reprobado.html', data)

def editarCursoReprobado(request, id):
    curso = get_object_or_404(CursoRepetido, id=id)
    data = {
        'form': CursoRepetidoForm(instance=curso)
    }

    if request.method == 'POST':
        formulario = CursoRepetidoForm(data=request.POST,instance=curso)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarCursoRepetido")
        else:
            data['form'] = formulario

    return render(request, 'cursosReprobados/editar-curso-reprobado.html', data)

def eliminarCursoReprobado(request, id):
    curso = get_object_or_404(CursoRepetido, id_curso=id)
    curso.delete()
    return redirect(to="listarCursoRepetido")

def listarCursoReprobado(request):
    cursos = CursoRepetido.objects.all()
    return render(request, 'cursosReprobados/listar-curso-reprobado.html', { 'cursos': cursos })


### MATRICULAS
@csrf_exempt
@api_view(['POST'])
def crearMatricula(request):
    # GET EXTRA DATA
    body = json.loads(request.body)
    genero = Genero.objects.get(id_genero=body['genero'])
    comuna = Comuna.objects.get(id_comuna=body['comuna'])
    estado_alumno = EstadoAlumno.objects.get(id_estado_alumno=1)

    # MATRICULA
    direccion = Direccion.objects.create(
        direccion = body['direccion'],
        numero = body['numero'],
        depto = body['depto'],
        block = body['block'],
        id_comuna = comuna)
    persona = Persona.objects.create(
        run = body['rut'],
        dv = body['dv'],
        p_nombre = body['p_nombre'],
        s_nombre = body['s_nombre'],
        app_paterno = body['app_paterno'],
        app_materno = body['app_materno'],
        nacionalidad = body['nacionalidad'],
        fecha_nac = body['fecha_nac'],
        id_genero = genero,
        id_direccion = direccion,
        telefono_fijo = body['telefono_fijo'],
        celular = body['celular'])
    matricula = Matricula.objects.create(
        curso_matricula = body['curso_matricula'])
    alumno = Alumno.objects.create(
        id_persona = persona,
        run = persona,
        id_matricula = matricula,
        id_estado_alumno = estado_alumno)
    
    # RESPONSE
    return Response({ 'ok': True, 'id_matricula': matricula.id_matricula })