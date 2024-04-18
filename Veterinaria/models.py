from django.db import models

# Create your models here.
class Duenos(models.Model):
    id_dueno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    correo = models.EmailField()

    status = models.CharField(max_length=10, choices=[('Active', 'ACTIVE'), ('Inactive', 'INACTIVE')], default='Active')

    class Meta:
        verbose_name_plural = "Duenos"

    def __str__(self):
        return self.nombre