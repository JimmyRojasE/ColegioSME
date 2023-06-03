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
    matricula = Matricula.objects.filter(id_matricula=id)
    if not matricula.exists():
        return redirect(to='inicio')

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
            datos_formulario=formulario.cleaned_data
            id_personalizado=datos_formulario
            print("formulario valido")
            formulario.save()
            return redirect(to="listarCurso")
        else:
           
            
            data["form"] = formulario
           
            print("formulario Invalido")

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

# def listarColegio(request):
#     colegios = Colegio.objects.all()
#     return render(request, 'colegio/listar-colegio.html', { 'cursos': colegios })

# def crearColegio(request):
#     data = {
#         'form':ColegioForm(),
#         'form2':DireccionForm()
#     }

#     if request.method == 'POST':
#         formulario = ColegioForm(data=request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect(to="listarColegio")
#         else:
#             data["form"] = formulario

#     return render(request, 'colegio/crear-colegio.html', data)

# def editarColegio(request, id):
#     colegio = get_object_or_404(Colegio, id_colegio=id)
#     data = {
#         'form': ColegioForm(instance=colegio)
#     }

#     if request.method == 'POST':
#         formulario = ColegioForm(data=request.POST,instance=colegio)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect(to="listarColegio")
#         data['form'] = formulario

#     return render(request, 'colegio/editar-colegio.html', data)

# def eliminarColegio(request, id):
#     curso = get_object_or_404(Colegio, id_colegio=id)
#     curso.delete()
#     return redirect(to="listarColegio")

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

def crearProfesor(request):
    return render(request, 'usuarios/crear-profesor.html')

# def crearCursoReprobado(request):
#     data = {
#         'form': CursoRepetidoForm()
#     }

#     if request.method == 'POST':
#         formulario = CursoRepetidoForm(data=request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect(to="listarCursoRepetido")
#         else:
#             data["form"] = formulario

#     return render(request, 'cursosReprobados/crear-curso-reprobado.html', data)

# def editarCursoReprobado(request, id):
#     curso = get_object_or_404(CursoRepetido, id=id)
#     data = {
#         'form': CursoRepetidoForm(instance=curso)
#     }

#     if request.method == 'POST':
#         formulario = CursoRepetidoForm(data=request.POST,instance=curso)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect(to="listarCursoRepetido")
#         else:
#             data['form'] = formulario

#     return render(request, 'cursosReprobados/editar-curso-reprobado.html', data)

# def eliminarCursoReprobado(request, id):
#     curso = get_object_or_404(CursoRepetido, id_curso=id)
#     curso.delete()
#     return redirect(to="listarCursoRepetido")

# def listarCursoReprobado(request):
#     cursos = CursoRepetido.objects.all()
#     return render(request, 'cursosReprobados/listar-curso-reprobado.html', { 'cursos': cursos })

def cursosAsistencia(request):
    return render(request, 'asistencia/cursos-asistencia.html')

def estudiantesAsistencia(request):
    return render(request, 'asistencia/estudiantes-asistencia.html')

def cursosNota(request):
    return render(request, 'notas/cursos-nota.html')

def estudiantesNota(request):
    return render(request, 'notas/estudiantes-nota.html')

def cursosAnotaciones(request):
    return render(request, 'anotaciones/cursos-anotaciones.html')

def estudiantesAnotaciones(request):
    return render(request, 'anotaciones/estudiantes-anotaciones.html')

## MATRICULAS (ESTUDIANTE)
@csrf_exempt
@api_view(['GET'])
def getPersona(request, run):
    try:
        persona = Persona.objects.get(run=run)
        direccion = Direccion.objects.get(id_direccion=persona.id_direccion.id_direccion)
        comuna = Comuna.objects.get(id_comuna=direccion.id_comuna.id_comuna)
        region = Region.objects.get(id_region=comuna.id_region.id_region)

        combined_data = {
            'rut': persona.run,
            'nombres': f'{persona.p_nombre} {persona.s_nombre}',
            'appaterno': persona.appaterno,
            'apmaterno': persona.apmaterno,
            'nacionalidad': persona.nacionalidad,
            'fecha_nacimiento': persona.fecha_nacimiento,
            'genero': persona.id_genero.id_genero,
            'nombre_calle': direccion.nombre_calle,
            'numero': direccion.numero,
            'region': region.nombre_region,
            'comuna': comuna.id_comuna,
            'telefono_fijo': persona.telefono_fijo,
            'celular': persona.celular
        }

        return Response(combined_data)
    except Persona.DoesNotExist as e:
        return Response({})

@csrf_exempt
@api_view(['POST'])
def crearMatricula(request):
    # GET DATA
    body = json.loads(request.body)
    genero = Genero.objects.get(id_genero=body['genero'])
    comuna = Comuna.objects.get(id_comuna=body['comuna'])
    curso = ListaCurso.objects.get(id_curso=body['curso_matricula'])
    estado_matricula = EstadoMatricula.objects.get(id_estado_matricula=1)
    estado_alumno = EstadoAlumno.objects.get(id_estado_alumno=1)

    persona = Persona.objects.filter(run=body['rut'])
    if persona.exists():
        direccion = Direccion.objects.filter(id_direccion=persona[0].id_direccion.id_direccion)

        direccion.update(
            nombre_calle = body['nombre_calle'],
            numero = body['numero'],
            id_comuna = comuna)
        persona.update(
            run = body['rut'],
            p_nombre = body['p_nombre'],
            s_nombre = body['s_nombre'],
            appaterno = body['appaterno'],
            apmaterno = body['apmaterno'],
            nacionalidad = body['nacionalidad'],
            fecha_nacimiento = body['fecha_nacimiento'],
            telefono_fijo = body['telefono_fijo'],
            celular = body['celular'],
            id_genero = genero,
            id_direccion = direccion[0].id_direccion)
        alumno = Alumno.objects.get(run=body['rut'])
        matricula = Matricula.objects.create(
            id_estado_matricula = estado_matricula,
            id_curso_matricula = curso,
            run_alumno = alumno)
        
        return Response({ 'ok': True, 'msg': 'Informacion actualizada', 'id_matricula': matricula.id_matricula })

    else:
        direccion = Direccion.objects.create(
            nombre_calle = body['nombre_calle'],
            numero = body['numero'],
            id_comuna = comuna)
        persona = Persona.objects.create(
            run = body['rut'],
            p_nombre = body['p_nombre'],
            s_nombre = body['s_nombre'],
            appaterno = body['appaterno'],
            apmaterno = body['apmaterno'],
            nacionalidad = body['nacionalidad'],
            fecha_nacimiento = body['fecha_nacimiento'],
            telefono_fijo = body['telefono_fijo'],
            celular = body['celular'],
            id_genero = genero,
            id_direccion = direccion)
        alumno = Alumno.objects.create(
            run = persona,
            id_estado_alumno = estado_alumno)
        matricula = Matricula.objects.create(
            id_estado_matricula = estado_matricula,
            id_curso_matricula = curso,
            run_alumno = alumno)
        
        return Response({ 'ok': True, 'msg': 'Informacion creada.', 'id_matricula': matricula.id_matricula })
    
### MATRICULAS (INFO ESTUDIANTE) ###
@csrf_exempt
@api_view(['GET'])
def obtenerInformacionExtra(request, id_matricula):
    matricula = Matricula.objects.get(id_matricula=id_matricula)
    alumno = Alumno.objects.get(run=matricula.run_alumno.run)

    combined_info = {
        'colegio_procedencia': alumno.colegio_procedencia,
        'razon_cambio_colegio': alumno.razon_cambio_colegio,
        'medio': alumno.medio,
        'estudiante_prioritario': alumno.estudiante_prioritario,
        'pie': alumno.pie,
        'evaluacion_profesional': alumno.evaluacion_profesional,
        'enfermedad_cronica': alumno.enfermedad_cronica,
        'ultimo_curso_aprobado': matricula.id_ultimo_curso_aprobado.id_curso
    }

    return Response(combined_info)

@csrf_exempt
@api_view(['PUT'])
def informacionAdicionalMatricula(request, id_matricula):
    body = json.loads(request.body)
    matricula = Matricula.objects.filter(id_matricula=id_matricula)
    alumno = Alumno.objects.filter(run=matricula[0].run_alumno.run.run)
    curso = ListaCurso.objects.get(id_curso=body['ultimo_curso_aprobado'])

    matricula.update(
        id_ultimo_curso_aprobado = curso.id_curso
    )
    alumno.update(
        colegio_procedencia = body['colegio_procedencia'],
        razon_cambio_colegio = body['razon_cambio_colegio'],
        medio = body['medio'],
        estudiante_prioritario = body['estudiante_prioritario'],
        pie = body['pie'],
        evaluacion_profesional = body['evaluacion_profesional'],
        enfermedad_cronica = body['enfermedad_cronica']
    )

    return Response({})

## USUARIOS
@csrf_exempt
@api_view(['POST'])
def creacionProfesor(request):
    body = json.loads(request.body)

    persona = Persona.objects.filter(run=body['rut'])
    genero = Genero.objects.get(id_genero=body['genero'])
    comuna = Comuna.objects.get(id_comuna=body['comuna'])

    if persona.exists():
        direccion = Direccion.objects.filter(id_direccion=persona[0].id_direccion.id_direccion)
        profesor = Profesor.objects.filter(run=persona[0].run)

        direccion.update(
            nombre_calle = body['nombre_calle'],
            numero = body['numero'],
            id_comuna = comuna)
        persona.update(
            p_nombre = body['p_nombre'],
            s_nombre = body['s_nombre'],
            appaterno = body['appaterno'],
            apmaterno = body['apmaterno'],
            nacionalidad = body['nacionalidad'],
            fecha_nacimiento = body['fecha_nacimiento'],
            telefono_fijo = body['telefono_fijo'],
            celular = body['celular'],
            id_genero = genero,
            id_direccion = direccion[0].id_direccion)
        profesor.update(
            grado_academico = body['grado_academico'],
            titulo = body['titulo'],
            mencion = body['mencion'],
            magister = body['magister'],
            doctorado = body['doctorado']
        )
        
        return Response({ 'msg': 'Informacion actualizada' })
    else:
        direccion = Direccion.objects.create(
            nombre_calle = body['nombre_calle'],
            numero = body['numero'],
            id_comuna = comuna)
        persona = Persona.objects.create(
            run = body['rut'],
            p_nombre = body['p_nombre'],
            s_nombre = body['s_nombre'],
            appaterno = body['appaterno'],
            apmaterno = body['apmaterno'],
            fecha_nacimiento = body['fecha_nacimiento'],
            nacionalidad = body['nacionalidad'],
            telefono_fijo = body['telefono_fijo'],
            celular = body['celular'],
            email = body['email'],
            id_direccion = direccion,
            id_genero = genero)
        profesor = Profesor.objects.create(
            run = persona,
            grado_academico = body['grado_academico'],
            titulo = body['titulo'],
            mencion = body['mencion'],
            magister = body['magister'],
            doctorado = body['doctorado']
        )

        return Response({ 'msg': 'Profesor creado' })
    
@csrf_exempt
@api_view(['GET'])
def getProfesor(request, run):
    try:
        persona = Persona.objects.get(run=run)
        profesor = Profesor.objects.get(run=persona.run)
        direccion = Direccion.objects.get(id_direccion=persona.id_direccion.id_direccion)
        comuna = Comuna.objects.get(id_comuna=direccion.id_comuna.id_comuna)
        region = Region.objects.get(id_region=comuna.id_region.id_region)

        combined_data = {
            'rut': persona.run,
            'nombres': f'{persona.p_nombre} {persona.s_nombre}',
            'appaterno': persona.appaterno,
            'apmaterno': persona.apmaterno,
            'nacionalidad': persona.nacionalidad,
            'fecha_nacimiento': persona.fecha_nacimiento,
            'genero': persona.id_genero.id_genero,
            'email': persona.email,
            'nombre_calle': direccion.nombre_calle,
            'numero': direccion.numero,
            'region': region.nombre_region,
            'comuna': comuna.id_comuna,
            'telefono_fijo': persona.telefono_fijo,
            'celular': persona.celular,
            'grado_academico': profesor.grado_academico, 
            'titulo': profesor.titulo, 
            'mencion': profesor.mencion, 
            'magister': profesor.magister, 
            'doctorado': profesor.doctorado
        }

        return Response(combined_data)
    except Persona.DoesNotExist as e:
        return Response({})