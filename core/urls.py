from django.urls import path
from .views import inicio, matriculasEst, matriculasApd, login,matriculasMdr,matriculasPdr,matriculasInfoest,crearCurso, crearProfesor,listarCurso,editarCurso,eliminarCurso
urlpatterns = [
    path('', inicio),
    path('matricula-est', matriculasEst),
    path('matricula-apd', matriculasApd),
    path('matricula-mdr', matriculasMdr),
    path('matricula-pdr', matriculasPdr),
    path('matricula-infoest', matriculasInfoest),
    path('crear-curso',crearCurso),
    path('crear-profesor',crearProfesor),
    path('login', login),
    path('listar-curso/', listarCurso, name="listarCurso"),
    path('eliminar-curso/<id>', eliminarCurso, name="eliminarCurso"),
    path('editar-curso/<id>/', editarCurso, name="editarCurso"),
    path('crear-curso/', crearCurso, name="crearCurso"),
]