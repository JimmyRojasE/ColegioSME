from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('matricula-est', matriculasEst),
    path('matricula-apd/<id>', matriculasApd),
    path('matricula-pdr/<id>', matriculasPdr),
    path('matricula-infoest/<id>', matriculasInfoest, name='matriculasInfoest'),
    path('crear-curso',crearCurso),
    path('crear-profesor',crearProfesor),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('listar-curso/', listarCurso, name="listarCurso"),
    path('eliminar-curso/<id>', eliminarCurso, name="eliminarCurso"),
    path('editar-curso/<id>', editarCurso, name="editarCurso"),
    path('crear-curso/', crearCurso, name="crearCurso"),
    path('listar-colegio/', listarColegio, name="listarColegio"),
    path('eliminar-colegio/<id>/<idmatricula>', eliminarColegio, name="eliminarColegio"),
    path('editar-colegio/<id>/<idmatricula>', editarColegio, name="editarColegio"),
    path('crear-colegio/', crearColegio, name="crearColegio"),
    path('listar-grupoFamiliar/<id>', listarGrupoFamiliar, name="listarGrupoFamiliar"),
    path('eliminar-grupoFamiliar/<id>', eliminarGrupoFamiliar, name="eliminarGrupoFamiliar"),
    path('editar-grupoFamiliar/<id>', editarGrupoFamiliar, name="editarGrupoFamiliar"),
    path('crear-grupoFamiliar/<id>', crearGrupoFamiliar, name="crearGrupoFamiliar"),
    path('eliminar-usuario/<id>', eliminarUsuario, name="eliminarUsuario"),
    path('editar-usuario/<id>', editarUsuario, name="editarUsuario"),
    path('crear-usuario/', crearUsuario, name="crearUsuario"),
    path('listar-usuario/', listarUsuario, name="listarUsuario"),
    path('eliminar-curso-reprobado/<id>', eliminarCursoReprobado, name="eliminarCursoReprobado"),
    path('editar-curso-reprobado/<id>', editarCursoReprobado, name="editarCursoReprobado"),
    path('crear-curso-reprobado/', crearCursoReprobado, name="crearCursoReprobado"),
    path('listar-curso-reprobado/', listarCursoReprobado, name="listarCursoReprobado"),


    ###
    # APIS
    ###
    path('crear-matricula-estudiante', crearMatricula, name='matricula-estudiante')
]