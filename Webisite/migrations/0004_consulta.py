# Generated by Django 5.1.2 on 2024-11-08 03:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webisite', '0003_remove_paciente_id_remove_paciente_idade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_Registro', models.DateTimeField(auto_now_add=True)),
                ('especialidade', models.CharField(choices=[('Psicologia Comportamental', 'Psicologia Comportamental'), ('Psicomotricidade', 'Psicomotricidade'), ('Fonoaudiologia', 'Fonoaudiologia'), ('Aplicadora em ABA', 'Aplicadora em ABA'), ('Estimulação Pedagógica', 'Estimulação Pedagógica')], default='Psicologia Comportamental', max_length=50)),
                ('id_Paciente_FK', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Webisite.paciente')),
                ('id_Voluntario_FK', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Webisite.voluntario')),
            ],
        ),
    ]
