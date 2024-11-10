# Generated by Django 5.1.2 on 2024-11-10 03:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webisite', '0012_eventos'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventos',
            name='descricao',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
