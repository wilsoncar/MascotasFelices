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
    id_mascota = models.AutoField(primary_key=True)
    id_dueno = models.ForeignKey(Duenos, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10, choices=[('Masculino', 'MASCULINO'), ('Femenino', 'FEMENINO')], default='Masculino')
    raza = models.CharField(max_length=25)
    edad = models.IntegerField()
    status = models.CharField(max_length=10, choices=[('Active', 'ACTIVE'), ('Inactive', 'INACTIVE')], default='Active')
    class Meta:
        verbose_name_plural = "Mascotas"
        
    def __str__(self):
        return self.nombre
    
class Citas(models.Model):
    id_cita = models.AutoField(primary_key=True)
    id_mascota = models.ForeignKey(Mascotas, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    tipo_cita = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=[('Done', 'DONE'), ('Canceled', 'CANCELED')], default='Done')
    class Meta:
        verbose_name_plural = "Citas"
        
    def __str__(self):
        return f'{self.id_mascota} - {self.fecha} - {self.hora} - {self.tipo_cita}'
        #return self.id_mascota + '' + self.fecha + '' + self.hora + '' + self.tipo_cita

class Desparasitaciones(models.Model):
    id_desparasitacion = models.AutoField(primary_key=True)
    id_mascota = models.ForeignKey(Mascotas, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    fecha = models.DateField()
    status = models.CharField(max_length=20, choices=[('Completado', 'COMPLETADO'), ('No completado', 'No completado')], default='Completado')
    class Meta:
        verbose_name_plural = "Desparasitaciones"
        
    def __str__(self):
        return f'{self.id_mascota} - {self.fecha} - {self.tipo}'

