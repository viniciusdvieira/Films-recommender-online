from django.db import models

# Create your models here.
class Filme(models.Model):
    id_filme = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    genero = models.CharField(max_length=50)
    ano = models.IntegerField()