# Generated by Django 5.1.2 on 2024-11-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webisite', '0008_consulta_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('Concluida', 'Concluida'), ('Rejeitado', 'Rejeitado')], default='pendente', max_length=10),
        ),
    ]
