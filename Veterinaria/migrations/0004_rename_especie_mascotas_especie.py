# Generated by Django 5.0.2 on 2024-04-18 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Veterinaria', '0003_alter_duenos_direccion_alter_duenos_nombre_mascotas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascotas',
            old_name='Especie',
            new_name='especie',
        ),
    ]
