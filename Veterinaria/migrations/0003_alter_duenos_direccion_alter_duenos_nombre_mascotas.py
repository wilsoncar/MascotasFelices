# Generated by Django 5.0.2 on 2024-04-18 01:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Veterinaria', '0002_rename_dueno_pk_duenos_id_dueno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duenos',
            name='direccion',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='duenos',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id_mascota', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('Especie', models.CharField(max_length=25)),
                ('sexo', models.CharField(choices=[('Masculino', 'MASCULINO'), ('Femenino', 'FEMENINO')], default='Masculino', max_length=10)),
                ('raza', models.CharField(max_length=25)),
                ('edad', models.IntegerField()),
                ('status', models.CharField(choices=[('Active', 'ACTIVE'), ('Inactive', 'INACTIVE')], default='Active', max_length=10)),
                ('id_dueno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Veterinaria.duenos')),
            ],
            options={
                'verbose_name_plural': 'Mascotas',
            },
        ),
    ]