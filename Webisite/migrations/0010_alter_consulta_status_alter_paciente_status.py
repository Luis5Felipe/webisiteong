# Generated by Django 5.1.2 on 2024-11-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webisite', '0009_paciente_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('ativo', 'Ativo'), ('concluído', 'Concluído')], default='pendente', max_length=10),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('ativo', 'Ativo'), ('concluído', 'Concluído')], default='pendente', max_length=10),
        ),
    ]
