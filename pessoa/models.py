from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

class Pessoa(models.Model):

    nome_completo = models.CharField(max_length=256)
    data_nascimento = models.DateField(null=True)
    ativa = models.BooleanField(default=True)
    