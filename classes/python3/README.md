<!-- {"layout": "title"} -->
# Django
## Visão geral e uso do Models
---
<!-- {"layout": "section-header", "slideHash": "django"} -->
# Django
## Introdução e Modelos

- Projetos vs Aplicações
- Iniciando um projeto
- Criação do Modelo de BD

---
## Django

- Framework Web, possui:
  - artefatos para o desenvolvimento de aplicações web de forma **rápida** e **segura**
  - Mapeamento Objeto-Relacional
- Este possui:
  - **projeto**: Um conjunto de configurações, templates, e outros códigos para sua aplicação rodar
  - Dentro do projeto, várias **aplicações**: conjunto de funcionalidades correlacionadas que podem ser reusadas ao longo do código

---
# Iniciando um **projeto**:
```
django-admin.py startproject primeiro_projeto
```
:::result
<br>

![](../../images/dir-django-project.png)
:::
---
- Iniciando um **app** do projeto
```
cd primeiro_projeto
django-admin startapp app_projeto
```
:::result
![](../../images/dir-django-app.png)
:::
---
## Models

- Colocamos no arquivo `models.py` o modelo que será salvo no Banco de Dados.
Para criarmos o modelo, no arquivo `models.py`:
- Representamos o modelo por **classes**
- Seus os atributos e seus relacionamos são modelados como **atributos estáticos** da classe
- Configuramos, no arquivo `settings.py`, a conexão com o Banco de Dados
- Executamos um comando para criar as tabelas/relacionamentos  no Banco de Dados

-
---
# Models - Comandos uteis
- Criar o script python para criação/alteração das tabelas: `python3 manage.py makemigrations`
- Executar os scripts que ainda não foram executados para criação/alteração das tabelas: `python3 manage.py migrate`
---
# Models - Tesouro
```python
class Tesouro(models.Model):
    nome = models.CharField(max_length=45)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    img_tesouro = models.ImageField(upload_to="imgs")

    def __str__(self):
        return self.nome+" quantidade: "+str(self.quantidade)+\
                " R$ "+str(self.valor)+" "+str(self.img_tesouro)
```

- [Veja documentação da classe Model](https://docs.djangoproject.com/en/3.0/ref/models/options/)
- [Veja documentação dos campos](https://docs.djangoproject.com/en/3.0/ref/models/fields/)

---
# Models - Configuração

Abra o console python com o ambiente do DJango já configurado:
```
python3 manage.py shell
```

Ou crie um Jupyter. O seguinte código deve ser executado (Django v. 3):
```python
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "primeiro_projeto.settings")
django.setup()
```
Importe a classe do Tesouro:
```
from app_projeto.models import Tesouro
```
---
# Models - Inserção

```python
  t1 = Tesouro(nome="Moedas de ouro",quantidade=4,\
              valor=2.4,img_tesouro="moedas.png")
  t1.save()
  Tesouro.objects.create(nome="Barril de rum",\
                        quantidade=3,valor=343,img_tesouro="rum.png")
  Tesouro.objects.bulk_create([\
                Tesouro(nome="Coroa",quantidade=1,\
                        valor=23.2,img_tesouro="coroa.png"),\
                Tesouro(nome="Calice",quantidade=3,\
                        valor=13.2,img_tesouro="calice.png")\
                        ])
```
---
# Models - busca
- Busca todos os registros:
```python
lista = Tesouro.objects.all()
```
- Busca apenas um registro (Caso não encontre o registro, é retornado erro):  
```python
t = Tesouro.objects.get(nome="Coroa")
```
- Busca um registro, caso não exista, o cria
```python
t,inseriu = Tesouro.objects.get_or_create(nome="Coroa Linda",quantidade=1,\
                                  valor=23.2,img_tesouro="coroa.png")
```
---
## Models busca (usando filtros)
```python
lista = Tesouro.objects.filter(nome="Coroa",quantidade=1)
Post.objects.filter(data_publicacao__year=2006)
```
- Busca por iniciais
```python
lista = Tesouro.objects.filter(nome__startswith="Coroa",quantidade=1)
```
  - Outros operadores de string: `istartswith`,`endswith`, `iendswith`, `icontains`, `iexact`

- Tesouros com valor menor que R$ 10: `lista = Tesouro.objects.filter(valor__lt=10)`
  - Outros operadores: `lte`: <=;  `gt`: >; `gte`:>=

---
## Models busca (usando filtros)
- Todos exceto um determinado elemento:
```python
lista = Tesouro.objects.exclude(nome__startswith="Coroa")
```
- Concatenando filtros: Dos tesouros que não começam com coroa, aqueles que possuem um valor menor que 10:
```python
lista = Tesouro.objects.exclude(nome__startswith="Coroa")\
                        .filter(valor__lt = 10)
```
----
## Outros comandos
- Limitar as 3 primeiras linhas:
```python
lista = Tesouro.objects.all()[:3]
```

- Do resultado na posição 2 **do vetor** até a posição 5:
```python
lista = Tesouro.objects.all()[2:5]
```
- Filtros com outros Campos (valor menor que a quantidade):
```python
from django.db.models import F
lista = Tesouro.objects.filter(valor__lt = F('quantidade'))
```
---
## Models - projeções
- Exibir apenas o nome e a quantidade:
  ```python
  lista = Tesouro.objects.all().values("nome","quantidade")
  ```
  - usar `values_list` para exibir no formato de vetor (e não dicionário)
  - ao final, use  `distinct()` para eliminar elementos repetidos

- [Veja a documentação de consultas](https://docs.djangoproject.com/en/3.0/topics/db/queries/)
---
## Models - Campos Calculados
- Campos calculados:
```python
from django.db.models import F,ExpressionWrapper,DecimalField

tipo_campo_calculado = DecimalField(max_digits=10,\
                                    decimal_places=2,\
                                    blank=True)

expressao_valor_total = ExpressionWrapper(F('valor')*F('quantidade'),\
                                          output_field=tipo_campo_calculado)

lista = Tesouro.objects.annotate(total=expressao_valor_total)
```
[Documentação do Django Expressions](https://docs.djangoproject.com/en/3.0/ref/models/expressions/)
---
- Obtém a quantidade total de tesouros:
```python
from django.db.models import Sum
Tesouro.objects.aggregate(Sum("quantidade"))
```

- Obtém, para cada nome, a quantidade total:
```python
from django.db.models import Sum
Tesouro.objects.values("nome").annotate(Sum("quantidade"))
```

- [Veja documentação](https://docs.djangoproject.com/en/3.0/topics/db/aggregation/)
- [Mais exemplos](https://medium.com/better-programming/django-annotations-and-aggregations-48685994d149)
---
## Exclusões e atualizações
```python
#atualiza o tesouro com nome 'coroa'
t = Tesouro.objects.get(nome="Coroa")
t.quantidade = 10
t.save()
```
- Use `.delete()` no final da consulta para deletar os elementos da determinada consulta
```python
Tesouro.objects.get(nome="Coroa").delete() #deleta elemento de nome "Coroa"
Tesouro.objects.filter(valor__lt=10).delete() #deleta elementos de valor menor que 10
Tesouro.objects.all().delete() #deleta todos os elementos
```
---
# Models - Exemplo completo - Classes


```python
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
```
---
# Models - Exemplo completo (2/2)
```python
class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    texto = models.TextField()
    data_publicacao = models.DateField()
    autores = models.ManyToManyField(Author)
    rating = models.IntegerField()

    def __str__(self):
        return self.titulo
```

---
## Criação

```python
from app_projeto.models import *
bloguinho = Blog.objects.create(nome="Bloguinho",sobre="Este é um blog")

autores = [Author(nome="hasan",email="hasan@cefetmg.br"),
                                      Author(nome="Alice",email="alice@email.com"),
                                     Author(nome="Bob",email="bob@email.com")]

for autor in autores:
  autor.save()

posts = [Post(blog=bloguinho,titulo="Meu primeiro post",rating=10, texto="la",data_publicacao=datetime.now()),
        Post(blog=bloguinho,titulo="Meu segundo post",rating=10, texto="la2",data_publicacao=datetime.now()),
        Post(blog=bloguinho,titulo="Meu terceiro post",rating=10, texto="la3",data_publicacao=datetime.now()),]

for post in posts:
    post.save()
#vincula os autores aos posts
posts[0].autores.add(autores[0])
posts[1].autores.add(autores[1])
posts[1].autores.add(autores[2])
posts[2].autores.add(autores[2])
```
---
## Consultas úteis

```python
#exibe o nome do blog e titulo do post
posts = Post.objects.values("blog__nome","titulo")
#Contabiliza o numero de posts por autor
#armazenado em post__count
autores = Author.objects.annotate(Count('post'))
```

---
## Integração de Django com uma Base de Dados Legada

- Configure o `settings.py` para acessar essa base de dados
- No terminal digite:
```
python manage.py inspectdb > models.py
```

- Com isso, o Django irá gerar automaticamente as classes do modelo e criar o
arquivo `models.py` com ela:

```python
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=70)
    class Meta:
       managed = False
       db_table = 'CENSUS_PERSONS'
```

- Recomendável: crie uma **aplicação** nova pra cada base de dados legada
- [Veja documentação](https://docs.djangoproject.com/en/3.0/howto/legacy-databases/)
---
## Recomendações

- Minimize o número  de consultas ao banco quando possível
- Use índice quando possível para facilitar consultas repetitivas (ex: busca por CPF, nome da cidade)
- Aprenda a [usar cache](https://docs.djangoproject.com/en/3.0/topics/cache/) para deixar as consultas ainda mais rápidas
- SQLLite: recomendável apenas para testes
- Use [Transações](https://docs.djangoproject.com/en/3.0/topics/db/transactions/) quando necessário
- [Deixe a base de dados normalizada](https://medium.com/@diegobmachado/normaliza%C3%A7%C3%A3o-em-banco-de-dados-5647cdf84a12) - ou seja, evite redundancia de dados
- Use as classes Django para alterar a estrutura do banco de dados

---
## Prática

- Objetivo: treinar criação de tabelas e operações no Banco de Dados por meio do framework Django

[Clique aqui e veja a especificação](https://github.com/daniel-hasan/cefet-web-grad/blob/master/assignments/tasks/models/README.md)
---
# Referências

1. https://docs.djangoproject.com
1. Elmasri, Ramez, Shamkant B. Navathe, and Marília Guimarães Pinheiro. "Sistemas de banco de dados." (2005): 355-361.
