# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Alumno(models.Model):
    run = models.ForeignKey('Persona', on_delete=models.CASCADE, primary_key=True, to_field='run')
    id_estado_alumno = models.ForeignKey('EstadoAlumno', on_delete=models.CASCADE, db_column='id_estado_alumno')
    estudiante_prioritario = models.BooleanField(default=False)
    enfermedad_cronica = models.CharField(max_length=255, null=True)
    seguro_escolar_particular = models.CharField(max_length=255, null=True)
    discapacidad_fisica = models.CharField(max_length=255, null=True)
    evaluacion_profesional = models.BooleanField(default=False)
    pie = models.BooleanField(default=False)

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=255)

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=255)
    id_region = models.ForeignKey('Region', on_delete=models.CASCADE, db_column='id_region');

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    id_lista_curso = models.ForeignKey('ListaCurso', on_delete=models.CASCADE, db_column='id_lista_curso')
    id_tipo_curso = models.ForeignKey('TipoCurso', on_delete=models.CASCADE, db_column='id_tipo_curso')
    profesor_jefe = models.ForeignKey('Profesor', on_delete=models.CASCADE, db_column='run_profesor_jefe')

class CursoRepetido(models.Model):
    id_curso_repetido = models.AutoField(primary_key=True)
    id_lista_curso = models.ForeignKey('ListaCurso', on_delete=models.CASCADE, db_column='id_lista_curso')
    anno_repitencia = models.IntegerField()
    run_alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE, db_column='run_alumno')

class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    nombre_calle = models.CharField(max_length=255)
    numero = models.IntegerField()
    id_comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE, db_column='id_comuna')

class EstadoAlumno(models.Model):
    id_estado_alumno = models.AutoField(primary_key=True)
    nombre_estado_alumno = models.CharField(max_length=255)

class EstadoMatricula(models.Model):
    id_estado_matricula = models.AutoField(primary_key=True)
    nombre_estado_matricula = models.CharField(max_length=255)

class EstadoUsuario(models.Model):
    id_estado_usuario = models.AutoField(primary_key=True)
    nombre_estado_usuario = models.CharField(max_length=255)

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nombre_genero = models.CharField(max_length=255)

class GrupoFamiliar(models.Model):
    id_grupo_familiar = models.AutoField(primary_key=True)
    nombre_familiar = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    parentesco = models.CharField(max_length=255)
    run_alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE, db_column='run_alumno')

class ListaCurso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=255)

class Matricula(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    id_estado_matricula = models.ForeignKey('EstadoMatricula', on_delete=models.CASCADE, db_column='id_estado_matricula')
    id_curso_matricula = models.ForeignKey('Curso', on_delete=models.CASCADE, db_column='id_curso_matricula', related_name='set_curso_matricula')
    run_alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE, db_column='run_alumno')
    colegio_procedencia = models.CharField(max_length=255)
    id_ultimo_curso_aprobado = models.ForeignKey('Curso', on_delete=models.CASCADE, db_column='id_ultimo_curso_aprobado', related_name='set_ultimo_curso_aprobado')
    razon_cambio_colegio = models.CharField(max_length=255)
    medio = models.CharField(max_length=255)

class Parentesco(models.Model):
    id_parentesco = models.AutoField(primary_key=True)
    nombre_parentesco = models.CharField(max_length=255)

class Persona(models.Model):
    run = models.IntegerField(primary_key=True)
    p_nombre = models.CharField(max_length=255)
    s_nombre = models.CharField(max_length=255)
    appaterno = models.CharField(max_length=255)
    apmaterno = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=255)
    telefono_fijo = models.BigIntegerField()
    celular = models.BigIntegerField()
    email = models.CharField(max_length=255, null=True)
    id_direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE, db_column='id_direccion')
    id_genero = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='id_genero')

class Profesor(models.Model):
    run = models.ForeignKey('Persona', on_delete=models.CASCADE, primary_key=True, db_column='run', to_field='run')
    grado_academico = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    mencion = models.CharField(max_length=50)
    magister = models.CharField(max_length=50, null=True)
    doctorado = models.CharField(max_length=50, null=True)

class Responsable(models.Model):
    run = models.ForeignKey('Persona', on_delete=models.CASCADE, primary_key=True, db_column='run', to_field='run')
    profesion = models.CharField(max_length=255)
    ocupacion = models.CharField(max_length=255)
    nivel_academico = models.CharField(max_length=255)
    vive_con_alumno = models.BooleanField()
    id_tipo_apoderado = models.ForeignKey('TipoApoderado', on_delete=models.CASCADE, db_column='id_tipo_apoderado')

class ResponsableAlumno(models.Model):
    id_responsable_alumno = models.AutoField(primary_key=True)
    run_responsable = models.ForeignKey('Responsable', on_delete=models.CASCADE, db_column='id_responsable', related_name='set_id_responsable')
    run_alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE, db_column='run_alumno', related_name='set_run_alumno')
    id_parentesco = models.ForeignKey('Parentesco', on_delete=models.CASCADE, db_column='id_parentesco')

class TipoApoderado(models.Model):
    id_tipo_apoderado = models.AutoField(primary_key=True)
    nombre_tipo_apoderado = models.CharField(max_length=255)

class TipoCurso(models.Model):
    id_tipo_curso = models.AutoField(primary_key=True)
    nombre_tipo_curso = models.CharField(max_length=2)

class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    nombre_tipo_usuario = models.CharField(max_length=255)

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=255)
    id_tipo_usuario = models.ForeignKey('TipoUsuario', on_delete=models.CASCADE, db_column='id_tipo_usuario')
    id_estado_usuario = models.ForeignKey('EstadoUsuario', on_delete=models.CASCADE, db_column='id_estado_usuario')    

#####################################################################################################################################
