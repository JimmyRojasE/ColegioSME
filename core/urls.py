from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('matricula-est', matriculasEst),
    path('matricula-apd/<id>', matriculasApd),
    path('matricula-pdr/<id>', matriculasPdr),
    path('matricula-infoest/<id>', matriculasInfoest, name='matriculasInfoest'),
    # path('crear-curso',crearCurso),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('listar-curso/', listarCurso, name="listarCurso"),
    path('eliminar-curso/<id>', eliminarCurso, name="eliminarCurso"),
    path('editar-curso/<id>', editarCurso, name="editarCurso"),
    path('crear-curso/', crearCurso, name="crearCurso"),
    # path('listar-colegio/', listarColegio, name="listarColegio"),
    # path('eliminar-colegio/<id>/<idmatricula>', eliminarColegio, name="eliminarColegio"),
    # path('editar-colegio/<id>/<idmatricula>', editarColegio, name="editarColegio"),
    # path('crear-colegio/', crearColegio, name="crearColegio"),
    path('listar-grupoFamiliar/<id>', listarGrupoFamiliar, name="listarGrupoFamiliar"),
    path('eliminar-grupoFamiliar/<id>', eliminarGrupoFamiliar, name="eliminarGrupoFamiliar"),
    path('editar-grupoFamiliar/<id>', editarGrupoFamiliar, name="editarGrupoFamiliar"),
    path('crear-grupoFamiliar/<id>', crearGrupoFamiliar, name="crearGrupoFamiliar"),
    # path('eliminar-curso-reprobado/<id>', eliminarCursoReprobado, name="eliminarCursoReprobado"),
    # path('editar-curso-reprobado/<id>', editarCursoReprobado, name="editarCursoReprobado"),
    # path('crear-curso-reprobado/', crearCursoReprobado, name="crearCursoReprobado"),
    # path('listar-curso-reprobado/', listarCursoReprobado, name="listarCursoReprobado"),
    path('cursos-asistencia/', cursosAsistencia, name="cursosAsistencia"),
    path('estudiantes-asistencia/', estudiantesAsistencia, name="estudiantesAsistencia"),
    path('cursos-nota/', cursosNota, name="cursosNota"),
    path('estudiantes-nota/', estudiantesNota, name="estudiantesNota"),
    path('cursos-anotaciones/', cursosAnotaciones, name="cursosAnotaciones"),
    path('estudiantes-anotaciones/', estudiantesAnotaciones, name="estudiantesAnotaciones"),

    ## USUARIOS ##
    path('listar-usuarios', listarUsuario, name='listar-usuarios'),
    path('crear-usuarios', crearUsuario, name='crear-usuarios'),
    path('editar-usuarios', editarUsuario, name='listar-usuarios'),
    path('eliminar-usuarios', eliminarUsuario, name='eliminar-usuarios'),
    path('crear-profesor', crearProfesor, name='crear-profesor'),

    ### API ###
    path('crear-matricula-estudiante', crearMatricula),
    path('obtener-persona/<run>', getPersona),
    path('obtener-info-extra/<id_matricula>', obtenerInformacionExtra),
    path('estudiante-info-extra/<id_matricula>', informacionAdicionalMatricula),
    path('getTeacherData/<run>', getProfesor),
    path('creacion-profesor', creacionProfesor)
]