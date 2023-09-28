from django.db import models
from espacos.models import Sala
# Create your models here.

class Avaliacao(models.Model):
    dt_cad = models.DateField(auto_now = True)
    comentario = models.TextField()
    nota = models.PositiveIntegerField()
    nome = models.TextField()
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

# def __str__(self):
#         return self.dt_cad