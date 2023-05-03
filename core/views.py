from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .forms import CursoForm

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def matriculasEst(request):
    return render(request, 'matricula/matricula-est.html')

def matriculasApd(request):
    return render(request, 'matricula/matricula-apd.html')

def matriculasMdr(request):
    return render(request, 'matricula/matricula-mdr.html')

def matriculasPdr(request):
    return render(request, 'matricula/matricula-pdr.html')

def matriculasInfoest(request):
    return render(request, 'matricula/matricula-infoest.html')

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

