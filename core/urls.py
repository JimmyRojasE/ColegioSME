from django.urls import path
from .views import inicio, matriculasEst, matriculasApd, login,matriculasMdr,matriculasPdr,crearCurso, crearProfesor
urlpatterns = [
    path('', inicio),
    path('matricula-est', matriculasEst),
    path('matricula-apd', matriculasApd),
    path('matricula-mdr', matriculasMdr),
    path('matricula-pdr', matriculasPdr),
    path('crear-curso',crearCurso),
    path('crear-profesor',crearProfesor),
    path('login', login)
]