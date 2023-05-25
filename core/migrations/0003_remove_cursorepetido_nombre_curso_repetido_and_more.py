# Generated by Django 4.2.1 on 2023-05-25 03:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_cursorepetido_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursorepetido',
            name='nombre_curso_repetido',
        ),
        migrations.AddField(
            model_name='cursorepetido',
            name='id_lista_curso',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='core.listacursos', verbose_name='Nombre Curso'),
        ),
        migrations.AddField(
            model_name='cursorepetido',
            name='id_matricula',
            field=models.ForeignKey(db_column='id_matricula', default=django.utils.timezone.now, on_delete=django.db.models.deletion.DO_NOTHING, to='core.matricula', verbose_name='Id Matricula'),
            preserve_default=False,
        ),
    ]
