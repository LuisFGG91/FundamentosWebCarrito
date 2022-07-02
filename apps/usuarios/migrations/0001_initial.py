# Generated by Django 3.2.13 on 2022-06-23 04:14

import apps.usuarios.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('romanNumber', models.CharField(max_length=120, verbose_name='roman Number')),
                ('number', models.IntegerField(verbose_name='numero')),
                ('codigo', models.CharField(max_length=5, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regiones',
                'db_table': 'users_region',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='logo.png', upload_to=apps.usuarios.models.upload_to)),
                ('imageBanner', models.ImageField(blank=True, default='logo.png', upload_to=apps.usuarios.models.upload_to_banner)),
                ('rut', models.CharField(help_text='Indique su RUT', max_length=13, verbose_name='Rut')),
                ('phone', models.CharField(help_text='Numero de Teléfono. ej: +56555555555', max_length=100, null=True, verbose_name='Teléfono')),
                ('fecha_nacimiento', models.DateField(help_text='Fecha de Nacimiento', null=True, verbose_name='Fec. Nac.')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], help_text='Masculino o Femenino', max_length=1, verbose_name='Sexo')),
                ('tipo_sangre', models.CharField(help_text='Tipo de Sangre. ej: ORH-', max_length=5, verbose_name='Tipo de Sangre')),
                ('direccion', models.CharField(default='', help_text='Dirección de Habitación', max_length=55, null=True, verbose_name='Domicilio')),
                ('numero', models.CharField(default='', help_text='Numero', max_length=8, null=True, verbose_name='Numero')),
                ('is_profesor', models.BooleanField(default=False, verbose_name='Es profesor')),
                ('is_alumno', models.BooleanField(default=False, verbose_name='Es alumno')),
                ('is_utp', models.BooleanField(default=False, verbose_name='Es utp')),
                ('comuna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.region')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'users_usuario',
            },
        ),
        migrations.CreateModel(
            name='UTPProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
            options={
                'verbose_name': 'UtpProfile',
                'verbose_name_plural': 'UtpsProfiles',
                'db_table': 'users_utp_profile',
            },
        ),
        migrations.CreateModel(
            name='ProfesorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autorizado_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autorizado_by_profesorprofile_related', to='usuarios.usuario')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
            options={
                'verbose_name': 'ProfesorProfile',
                'verbose_name_plural': 'ProfesorProfiles',
                'db_table': 'users_profesor_profile',
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('codigo', models.CharField(max_length=120, verbose_name='roman Number')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.region')),
            ],
            options={
                'verbose_name': 'Comuna',
                'verbose_name_plural': 'Comunas',
                'db_table': 'users_comuna',
            },
        ),
        migrations.CreateModel(
            name='AlumnoProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
            options={
                'verbose_name': 'AlumnosProfile',
                'verbose_name_plural': 'AlumnosProfiles',
                'db_table': 'users_alumno_profile',
            },
        ),
    ]
