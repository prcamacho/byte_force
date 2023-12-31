# Generated by Django 4.2.1 on 2023-06-21 21:45

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('dni', models.BigIntegerField(unique=True)),
                ('imagen', models.ImageField(default='usuariopordefecto.png', upload_to='coordinadores/')),
                ('activo', models.BooleanField(default=True)),
                ('empleado', models.BooleanField(default=True)),
                ('fecha_alta', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
