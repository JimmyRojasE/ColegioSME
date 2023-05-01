from django.urls import path
from .views import inicio, matriculasEst, matriculasApd, login,matriculasMdr,matriculasPdr,matriculasInfoest,crearCurso, crearProfesor
urlpatterns = [
    path('', inicio),
    path('matricula-est', matriculasEst),
    path('matricula-apd', matriculasApd),
    path('matricula-mdr', matriculasMdr),
    path('matricula-pdr', matriculasPdr),
    path('matricula-infoest', matriculasInfoest),
    path('crear-curso',crearCurso),
    path('crear-profesor',crearProfesor),
    path('login', login)
]