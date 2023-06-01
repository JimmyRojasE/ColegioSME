from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.signals import post_save 
from .models import Curso, Colegio, Direccion, GrupoFamiliar, Persona, CursoRepetido,Usuario
from .forms import CursoForm, ColegioForm, DireccionForm, GrupoFamiliarForm, CursoRepetidoForm,UsuarioForm
from django.contrib import messages

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
    data={
        'form':UsuarioForm()
    }
    if request.method=='POST':
        try:
            usuario=Usuario.objects.get(id_usuario=request.POST['id_usuario'], password=request.POST['password'])
            persona=Persona.objects.get(run=request.POST['id_usuario'])
            nombre=persona.p_nombre + ' ' + persona.app_paterno            
            request.user={
                'nombre':nombre,
                'id':usuario.id_usuario,
                'rol':usuario.id_rol_usuario.id_rol_usuario,
                'estado':usuario.id_estado_usuario.id_estado_usuario,
            }

            return render(request,'index.html')
        
        except Usuario.DoesNotExist as e:
            messages.success(request,'Usuario o Password Incorrectos..')
        except Persona.DoesNotExist as e:
            messages.success(request,'Falta Ingresar Datos Personales..')
        except :
            messages.success(request,'Ingrese Información Válida ..')
    return render(request, 'auth/login.html',data)

def logout(request):
    try:
        del request.session['nombre']
    except:
        return render(request,'index.html')
    return render(request,'index.html')



def crearProfesor(request):
    return render(request, 'profesor/crear-profesor.html')

def listarCurso(request):
    cursos=Curso.objects.all()
    data={
        'Cursos':cursos
    }

    return render(request,'curso/listar-cursos.html',data)

def crearCurso(request):
    data={
    'form':CursoForm()
    }
    if request.method=='POST':
        formulario=CursoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarCurso")
        else:
            data["form"]=formulario

    return render(request,'curso/crear-curso.html',data)

def editarCurso(request,id):

    curso=get_object_or_404(Curso,id_curso=id)
    data={
        'form': CursoForm(instance=curso)
    }
    if request.method=='POST':
        formulario=CursoForm(data=request.POST,instance=curso)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarCurso")
        data['form']=formulario

    return render(request,'curso/editar-curso.html',data)

def eliminarCurso(request,id):
    curso=get_object_or_404(Curso,id_curso=id)
    curso.delete()
    return redirect(to="listarCurso")

def crearDireccion(request):
    
    data={
    'form':DireccionForm()
    }
    if request.method=='POST':
        formulario=DireccionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            dato=Direccion.objects.last()
            data={
                'direccion':dato
            }
            return redirect( to='crearColegio',id='{dato.id_direccion}')
        else:
            data["form"]=formulario

    return render(request,'direccion/crear-direccion.html',data)

def listarColegio(request):
    colegios=Colegio.objects.all()
    data={
        'Cursos':colegios
    }

    return render(request,'colegio/listar-colegio.html',data)

def crearColegio(request):
    
    data={
    'form':ColegioForm(),
    }
    if request.method=='POST':
        formulario=ColegioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarColegio")
        else:
            data["form"]=formulario

    return render(request,'colegio/crear-colegio.html',data)

def editarColegio(request,id):

    colegio=get_object_or_404(Colegio,id_colegio=id)
    data={
        'form': ColegioForm(instance=colegio)
    }
    if request.method=='POST':
        formulario=ColegioForm(data=request.POST,instance=colegio)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarColegio")
        data['form']=formulario

    return render(request,'colegio/editar-colegio.html',data)

def eliminarColegio(request,id):
    curso=get_object_or_404(Colegio,id_colegio=id)
    curso.delete()
    return redirect(to="listarColegio")

def listarGrupoFamiliar(request,id):
    grupoFamiliar=GrupoFamiliar.objects.filter(id_matricula=id)
    # grupoFamiliar=get_object_or_404(GrupoFamiliar,id_matricula=id)
    data={
        'grupoFamiliar': grupoFamiliar,
        'id_matricula': id
    }

    return render(request, 'grupoFamiliar/listar-grupoFamiliar.html', data)

def crearGrupoFamiliar(request, id):
    data = {
        'form': GrupoFamiliarForm(initial= { 'id_matricula': id } ),
        'id_matricula': id
    }

    if request.method=='POST':
        formulario=GrupoFamiliarForm(data=request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect(to=f"/listar-grupoFamiliar/{id}")
        else:
            data["form"]=formulario

    return render(request,'grupoFamiliar/crear-grupoFamiliar.html',data)

def editarGrupoFamiliar(request,id,idmatricula):

    grupofamiliar=get_object_or_404(GrupoFamiliar,id_gr_fam=id)
    data={
        'form': GrupoFamiliarForm(instance=grupofamiliar)
    }
    if request.method=='POST':
        formulario=GrupoFamiliarForm(data=request.POST,instance=grupofamiliar)
        if formulario.is_valid():
            formulario.save()
            return redirect(to=f"/listar-grupoFamiliar/{idmatricula}")
        data['form']=formulario

    return render(request,'grupoFamiliar/editar-grupoFamiliar.html',data)

def eliminarGrupoFamiliar(request,id,idmatricula):
    curso=get_object_or_404(GrupoFamiliar,id_gr_fam=id)
    curso.delete()
    return redirect(to=f"listarGrupoFamiliar/{idmatricula}")

def crearUsuario(request):
    return render(request,'usuarios/crear-usuario.html')

def listarUsuario(request):
    personas=Persona.objects.all()
    data={
        'Personas':personas
    }
    return render(request,'usuarios/listar-usuario.html',data)

def editarUsuario(request):
    return render(request,'usuarios/editar-usuario.html')

def eliminarUsuario(request, id):
    return redirect(to="listarUsuario")

def crearCursoReprobado(request):
    data={
    'form':CursoRepetidoForm()
    }
    if request.method=='POST':
        formulario=CursoRepetidoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarCursoRepetido")
        else:
            data["form"]=formulario

    return render(request,'cursosReprobados/crear-curso-reprobado.html',data)



def editarCursoReprobado(request,id):

    curso=get_object_or_404(CursoRepetido,id=id)
    data={
        'form': CursoRepetidoForm(instance=curso)
    }
    if request.method=='POST':
        formulario=CursoRepetidoForm(data=request.POST,instance=curso)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarCursoRepetido")
        data['form']=formulario

    return render(request,'cursosReprobados/editar-curso-reprobado.html',data)

def eliminarCursoReprobado(request,id):
    curso=get_object_or_404(CursoRepetido,id=id)
    curso.delete()
    return redirect(to="listarCursoRepetido")

def listarCursoReprobado(request):
    cursosRepetidos=CursoRepetido.objects.all()
    data={
        'CursosR':cursosRepetidos
    }

    return render(request,'cursosReprobados/listar-curso-reprobado.html',data)
