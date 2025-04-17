from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    correo = models.CharField(max_length=250)
    contra = models.CharField(max_length=250)

    def __str__(self):
        return self.correo
