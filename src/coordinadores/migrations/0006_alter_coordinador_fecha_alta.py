# Generated by Django 4.2.1 on 2023-05-26 03:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinadores', '0005_alter_coordinador_fecha_alta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinador',
            name='fecha_alta',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 26, 0, 41, 5, 940750)),
        ),
    ]
