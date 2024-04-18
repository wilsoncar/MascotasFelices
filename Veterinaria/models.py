from django.db import models

# Create your models here.
class Duenos(models.Model):
    id_dueno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=250)
    telefono = models.IntegerField()
    correo = models.EmailField()
    status = models.CharField(max_length=10, choices=[('Active', 'ACTIVE'), ('Inactive', 'INACTIVE')], default='Active')
    class Meta:
        verbose_name_plural = "Duenos"

    def __str__(self):
        return self.nombre

class Mascotas(models.Model):
    id_dueno = models.ForeignKey(Duenos, on_delete=models.CASCADE)
    id_mascota = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10, choices=[('Masculino', 'MASCULINO'), ('Femenino', 'FEMENINO')], default='Masculino')
    raza = models.CharField(max_length=25)
    edad = models.IntegerField()
    status = models.CharField(max_length=10, choices=[('Active', 'ACTIVE'), ('Inactive', 'INACTIVE')], default='Active')
    class Meta:
        verbose_name_plural = "Mascotas"
        
    def __str__(self):
        return self.nombre
