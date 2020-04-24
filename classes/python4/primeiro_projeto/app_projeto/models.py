from django.db import models

# Create your models here.
class Pessoa(models.Model):
  nome = models.CharField(max_length=100)
  data_nascimento = models.DateField()
  def __str__(self):
      return f"{self.nome} - {self.data_nascimento}"
      
