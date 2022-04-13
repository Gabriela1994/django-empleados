# Generated by Django 4.0.4 on 2022-04-12 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('shor_name', models.CharField(max_length=50, verbose_name='Nombre Corto')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
        ),
    ]
