# Generated by Django 5.1.2 on 2024-11-08 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webisite', '0004_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='id_Paciente',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='voluntario',
            name='id_Voluntario',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
