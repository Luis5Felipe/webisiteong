# Generated by Django 5.1.2 on 2024-11-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webisite', '0013_eventos_data_eventos_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='MidiaEventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_evento', models.DateField()),
                ('fotos', models.ImageField(blank=True, null=True, upload_to='eventos/')),
            ],
        ),
        migrations.DeleteModel(
            name='Eventos',
        ),
    ]
