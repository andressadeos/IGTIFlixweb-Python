from django.db import models


# Create your models here.
class Serie(models.Model):
    idGenero = models.ForeignKey("genero.Genero", on_delete=models.PROTECT)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


