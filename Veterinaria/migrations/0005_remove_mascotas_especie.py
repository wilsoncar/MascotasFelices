# Generated by Django 5.0.2 on 2024-04-18 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Veterinaria', '0004_rename_especie_mascotas_especie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascotas',
            name='especie',
        ),
    ]
