# Generated by Django 5.1.2 on 2024-11-10 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webisite', '0011_alter_consulta_status_alter_paciente_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagens', models.ImageField(blank=True, null=True, upload_to='Website/')),
            ],
        ),
    ]