from django.db import models

class Pessoa(models.Model):
  nome = models.CharField(max_length=100)
  data_nascimento = models.DateField()
  def __str__(self):
      return f"{self.nome} - {self.data_nascimento}"
# Create your models here.
class Blog(models.Model):
    nome = models.CharField(max_length=100)
    sobre = models.TextField()

    def __str__(self):
        return self.nome

class Author(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    texto = models.TextField()
    data_publicacao = models.DateField()
    autores = models.ManyToManyField(Author)
    rating = models.IntegerField()

    def __str__(self):
        return self.titulo

class Tesouro(models.Model):
    nome = models.CharField(max_length=45, unique=True)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    img_tesouro = models.ImageField(upload_to="imgs", null=True)

    def __str__(self):
        return self.nome+" quantidade: "+str(self.quantidade)+\
                " R$ "+str(self.valor)+" "+str(self.img_tesouro)
