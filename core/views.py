from django.shortcuts import render

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

def login(request):
    return render(request, 'auth/login.html')

def crearCurso(request):
    return render(request, 'curso/crear-curso.html')
    
def crearProfesor(request):
    return render(request, 'profesor/crear-profesor.html')