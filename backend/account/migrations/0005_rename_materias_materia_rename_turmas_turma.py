# Generated by Django 4.0.3 on 2023-11-25 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_turmas_horas_alter_turmas_turma'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Materias',
            new_name='Materia',
        ),
        migrations.RenameModel(
            old_name='Turmas',
            new_name='Turma',
        ),
    ]
