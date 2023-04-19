from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def matriculasEst(request):
    return render(request, 'matricula/matricula-est.html')

def matriculasApd(request):
    return render(request, 'matricula/matricula-apd.html')

def login(request):
    return render(request, 'auth/login.html')