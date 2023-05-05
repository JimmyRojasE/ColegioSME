# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Administrador(models.Model):
    id_persona = models.OneToOneField('Persona', models.DO_NOTHING, unique=True,db_column='id_persona', primary_key=True)  # The composite primary key (id_persona, run) found, that is not supported. The first column is selected.
    grado_academico = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    mencion = models.CharField(max_length=50)
    magister = models.CharField(max_length=50, blank=True, null=True)
    doctorado = models.CharField(max_length=50, blank=True, null=True)
    run = models.ForeignKey('Persona', models.DO_NOTHING, db_column='run', unique=True, to_field='run', related_name='administrador_run_set')
    cargo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'administrador'
        unique_together = (('id_persona', 'run'),)


class Alumno(models.Model):
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, unique=True, db_column='id_persona')
    etnia = models.CharField(max_length=30, blank=True, null=True)
    estudiante_prioritario = models.IntegerField()
    enfermedad_cronica = models.CharField(max_length=50, blank=True, null=True)
    seguro_escolar_particular = models.CharField(max_length=50, blank=True, null=True)
    run = models.OneToOneField('Persona', models.DO_NOTHING, db_column='run', unique=True, primary_key=True, related_name='alumno_run_set')  # The composite primary key (run, id_persona) found, that is not supported. The first column is selected.
    discapacidad_fisica = models.CharField(max_length=50, blank=True, null=True)
    id_matricula = models.OneToOneField('Matricula', models.DO_NOTHING, db_column='id_matricula')
    id_estado_alumno = models.ForeignKey('EstadoAlumno', models.DO_NOTHING, db_column='id_estado_alumno')
    pie = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alumno'
        unique_together = (('run', 'id_persona'),)


class AlumnoAsignatura(models.Model):
    id_alumno_asignatura = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Alumno, models.DO_NOTHING , unique=True, db_column='id_persona', to_field='id_persona')
    run = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='run', unique=True, related_name='alumnoasignatura_run_set')
    id_asignatura = models.ForeignKey('Asignatura', models.DO_NOTHING, db_column='id_asignatura')
    id_asistencia = models.OneToOneField('Asistencia', models.DO_NOTHING, db_column='id_asistencia')

    class Meta:
        managed = False
        db_table = 'alumno_asignatura'


class Anotaciones(models.Model):
    id_anotación = models.AutoField(primary_key=True)
    descripción_anotación = models.CharField(max_length=1000)
    id_tipo_anotacion = models.ForeignKey('TipoAnotacion', models.DO_NOTHING, db_column='id_tipo_anotacion')
    run = models.IntegerField()
    id_persona = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anotaciones'


class Apoderado(models.Model):
    id_persona = models.OneToOneField('Persona', models.DO_NOTHING, unique=True, db_column='id_persona', primary_key=True)  # The composite primary key (id_persona, run) found, that is not supported. The first column is selected.
    profesion = models.CharField(max_length=40)
    ocupación = models.CharField(max_length=40)
    nivel_academico = models.CharField(max_length=50)
    run = models.ForeignKey('Persona', models.DO_NOTHING, db_column='run', unique=True, to_field='run', related_name='apoderado_run_set')
    id_tipo_apoderado = models.ForeignKey('TipoApoderado', models.DO_NOTHING, db_column='id_tipo_apoderado')

    class Meta:
        managed = False
        db_table = 'apoderado'
        unique_together = (('id_persona', 'run'),)


class ApoderadoAlumno(models.Model):
    id_apod_alum = models.AutoField(primary_key=True)
    vive_con_alumno = models.IntegerField()
    id_persona = models.ForeignKey(Apoderado, models.DO_NOTHING, unique=True, db_column='id_persona')
    run = models.ForeignKey(Apoderado, models.DO_NOTHING, db_column='run', unique=True, to_field='run', related_name='apoderadoalumno_run_set')
    id_persona1 = models.ForeignKey(Alumno, models.DO_NOTHING, unique=True, db_column='id_persona1', to_field='id_persona')
    run1 = models.ForeignKey(Alumno, models.DO_NOTHING, unique=True, db_column='run1', related_name='apoderadoalumno_run1_set')
    id_parentesco = models.ForeignKey('Parentesco', models.DO_NOTHING, db_column='id_parentesco')

    class Meta:
        managed = False
        db_table = 'apoderado_alumno'


class Asignatura(models.Model):
    id_asignatura = models.AutoField(primary_key=True)
    nombre_asignatura = models.CharField(max_length=50)
    cantidad_de_horas = models.IntegerField()
    id_curso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='id_curso')
    id_calificacion = models.ForeignKey('Calificacion', models.DO_NOTHING, db_column='id_calificacion')

    class Meta:
        managed = False
        db_table = 'asignatura'


class Asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    nombre_asistencia = models.CharField(max_length=50)
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'asistencia'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    nota = models.IntegerField(blank=True, null=True)
    descripción_nota = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calificacion'


class CobroEstudiantil(models.Model):
    id_cobro = models.AutoField(primary_key=True)
    fecha_de_pago = models.DateField()
    precio = models.IntegerField()
    id_matricula = models.ForeignKey('Matricula', models.DO_NOTHING, db_column='id_matricula')

    class Meta:
        managed = False
        db_table = 'cobro_estudiantil'


class Colegio(models.Model):
    id_colegio = models.AutoField(primary_key=True)
    nombre_colegio = models.CharField(max_length=50)
    representante_legal = models.CharField(max_length=50)
    telefono = PhoneNumberField()
    id_direccion = models.ForeignKey('Direccion', models.DO_NOTHING, db_column='id_direccion')

    class Meta:
        managed = False
        db_table = 'colegio'


class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=50)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')

    class Meta:
        managed = False
        db_table = 'comuna'


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=50)
    año = models.IntegerField()
    cantidad_matricula = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'curso'


class CursoRepetido(models.Model):
    id_curso_repetido = models.AutoField(primary_key=True)
    nombre_curso_repetido = models.CharField(max_length=50)
    anno_repitencia = models.IntegerField()
    id_matricula = models.ForeignKey('Matricula', models.DO_NOTHING, db_column='id_matricula')

    class Meta:
        managed = False
        db_table = 'curso_repetido'


class DetallePago(models.Model):
    id_detalle_pago = models.AutoField(primary_key=True)
    id_pago = models.ForeignKey('Pago', models.DO_NOTHING, db_column='id_pago')
    id_cobro = models.ForeignKey(CobroEstudiantil, models.DO_NOTHING, db_column='id_cobro')

    class Meta:
        managed = False
        db_table = 'detalle_pago'


class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=25)
    numero = models.CharField(max_length=9, blank=True, null=True)
    depto = models.IntegerField(blank=True, null=True)
    block = models.CharField(max_length=10, blank=True, null=True)
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')

    class Meta:
        managed = False
        db_table = 'direccion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EstadoAlumno(models.Model):
    id_estado_alumno = models.AutoField(primary_key=True)
    nombre_estado_alumno = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'estado_alumno'


class EstadoUsuario(models.Model):
    id_estado_usuario = models.AutoField(primary_key=True)
    nombre_estado_usuario = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'estado_usuario'


class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nombre_genero = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'genero'


class GrupoFamiliar(models.Model):
    id_gr_fam = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    parentesco = models.CharField(max_length=25)
    id_matricula = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'grupo_familiar'


class Matricula(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    curso_matricula = models.CharField(max_length=50)
    colegio_procedencia = models.CharField(max_length=50)
    ultimo_curso_aprobado = models.CharField(max_length=50)
    anno_curso_aprobado = models.IntegerField()
    razon_cambio_colegio = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matricula'


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    fecha_pago = models.DateField()
    monto_total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pago'


class Parentesco(models.Model):
    id_parentesco = models.AutoField(primary_key=True)
    nombre_parentesco = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'parentesco'


class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True , unique=True)  # The composite primary key (id_persona, run) found, that is not supported. The first column is selected.
    p_nombre = models.CharField(max_length=30)
    s_nombre = models.CharField(max_length=30, blank=True, null=True)
    app_paterno = models.CharField(max_length=30)
    app_materno = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    run = models.IntegerField( unique=True)
    dv = models.CharField(max_length=1)
    nacionalidad = models.CharField(max_length=30)
    telefono_fijo = models.IntegerField()
    celular = models.IntegerField()
    email = models.CharField(max_length=50, blank=True, null=True)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, db_column='id_direccion')
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE, db_column='id_genero')

    class Meta:
        managed = False
        db_table = 'persona'
        unique_together = (('id_persona', 'run'),)


class Profesor(models.Model):
    id_persona = models.OneToOneField(Persona, models.DO_NOTHING, db_column='id_persona',unique=True, primary_key=True)  # The composite primary key (id_persona, run) found, that is not supported. The first column is selected.
    grado_academico = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    mencion = models.CharField(max_length=50)
    magister = models.CharField(max_length=50, blank=True, null=True)
    doctorado = models.CharField(max_length=50, blank=True, null=True)
    run = models.ForeignKey(Persona, models.DO_NOTHING, db_column='run', to_field='run',unique=True, related_name='profesor_run_set')

    class Meta:
        managed = False
        db_table = 'profesor'
        unique_together = (('id_persona', 'run'),)


class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'region'


class RolUsuario(models.Model):
    id_rol_usuario = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rol_usuario'


class TipoAnotacion(models.Model):
    id_tipo_anotacion = models.AutoField(primary_key=True)
    tipo_anotacion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_anotacion'


class TipoApoderado(models.Model):
    id_tipo_apoderado = models.AutoField(primary_key=True)
    tipo_apoderado = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_apoderado'


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=20)
    id_rol_usuario = models.ForeignKey(RolUsuario, models.DO_NOTHING, db_column='id_rol_usuario')
    id_estado_usuario = models.ForeignKey(EstadoUsuario, models.DO_NOTHING, db_column='id_estado_usuario')

    class Meta:
        managed = False
        db_table = 'usuario'
