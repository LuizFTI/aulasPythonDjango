from django.db import models

# Create your models here.

class Fonte(models.Model):

    descricao = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)