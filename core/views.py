from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso,Colegio,Direccion,GrupoFamiliar,Persona,CursoRepetido
from .forms import CursoForm,ColegioForm, DireccionForm,GrupoFamiliarForm,CursoRepetidoForm

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def matriculasEst(request):
    return render(request, 'matricula/matricula-est.html')

def matriculasInfoest(request):
    return render(request, 'matricula/matricula-infoest.html')

def matriculasMdr(request):
    return render(request, 'matricula/matricula-mdr.html')

def matriculasPdr(request):
    return render(request, 'matricula/matricula-pdr.html')

def matriculasApd(request):
    return render(request, 'matricula/matricula-apd.html')

def login(request):
    return render(request, 'auth/login.html')

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

def listarColegio(request):
    colegios=Colegio.objects.all()
    data={
        'Cursos':colegios
    }

    return render(request,'colegio/listar-colegio.html',data)

def crearColegio(request):
    data={
    'form':ColegioForm(),
    'form2':DireccionForm()
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

def listarGrupoFamiliar(request):
    grupoFamiliar=GrupoFamiliar.objects.all()
    data={
        'grupoFamiliar':grupoFamiliar
    }

    return render(request,'grupoFamiliar/listar-grupoFamiliar.html',data)

def crearGrupoFamiliar(request):
    data={
    'form':GrupoFamiliarForm(),
    
    }
    if request.method=='POST':
       formulario=GrupoFamiliarForm(data=request.POST)
       if formulario.is_valid():
           formulario.save()
           return redirect(to="listarGrupoFamiliar")
       else:
           data["form"]=formulario

    return render(request,'grupoFamiliar/crear-grupoFamiliar.html',data)

def editarGrupoFamiliar(request,id):

    grupofamiliar=get_object_or_404(GrupoFamiliar,id_gr_fam=id)
    data={
        'form': GrupoFamiliarForm(instance=grupofamiliar)
    }
    if request.method=='POST':
        formulario=GrupoFamiliarForm(data=request.POST,instance=grupofamiliar)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarGrupoFamiliar")
        data['form']=formulario

    return render(request,'grupoFamiliar/editar-grupoFamiliar.html',data)

def eliminarGrupoFamiliar(request,id):
    curso=get_object_or_404(GrupoFamiliar,id_gr_fam=id)
    curso.delete()
    return redirect(to="listarGrupoFamiliar")

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

def crearCursoRepetido(request):
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

    return render(request,'curso/crear-curso-repetido.html',data)

def editarCursoRepetido(request,id):

    curso=get_object_or_404(CursoRepetido,id_curso=id)
    data={
        'form': CursoRepetidoForm(instance=curso)
    }
    if request.method=='POST':
        formulario=CursoRepetidoForm(data=request.POST,instance=curso)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarCursoRepetido")
        data['form']=formulario

    return render(request,'curso/editar-curso-repetido.html',data)

def eliminarCursoRepetido(request,id):
    curso=get_object_or_404(CursoRepetido,id_curso=id)
    curso.delete()
    return redirect(to="listarCursoRepetido")

def listarCursoRepetido(request):
    cursosRepetidos=CursoRepetido.objects.all()
    data={
        'CursosR':cursosRepetidos
    }

    return render(request,'colegio/listar-cursos-repetidos.html',data)
