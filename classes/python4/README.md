<!-- {"layout": "title"} -->
# Django Templates e Views
## Templates, Views, arquivos estáticos e URLs
---
## Principais Componentes  Django

- **Template**: Exibição do html (usualmente, dinâmico)
- **View**: Obtenção da resposta e renderização do **template**. Se necessário, consultando o banco de dados pelos **models**
- **Models**: Responsável pela persistência/gerenciamento dos dados


---
## Arquivos do projeto

![](../../images/dir-django-app.png)

---
## Templates

- Facilita a geração de páginas dinâmicas

- Possui:
  - Parte estática do conteúdo
  - Sintaxe para tratar a parte dinâmica

- **Sintaxe para apresentação**: Não é possível executar códigos Python no template.
---
## Templates - Exemplo na linha de comando

```python
>>> from django.template import engines
>>> django_engine = engines['django']
>>> template = django_engine.from_string("Ola {{ name }}!")
>>> template.render({'name':'Hasan'})
'Ola Hasan!'
```

---
## Templates - Configuração

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'dir_templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            # ... some options here ...
        },
    },
]
```
- [Veja opções do atributo **options** aqui](https://docs.djangoproject.com/en/2.1/topics/templates/#django.template.backends.django.DjangoTemplates)

---
<!-- {"layout": "2-column-content"} -->
## Template inclusão e herança de templates
```html
<html>
  <head>
    <title>Pagina Supimpa - Home</title>
    <link rel="stylesheet" href="estilos.css">
  </head>
  <body>
    <nav><ul><li>Home</li><li>História</li></ul>
    <main>conteudo do home :D</main>
  <body>
</html>
```
```html
<html>
  <head>
    <title>Pagina Supimpa - História</title>
    <link rel="stylesheet" href="estilos.css">
  </head>
  <body>
    <nav><ul><li>Home</li><li>História</li></ul>
    <main>conteudo da história :D</main>
  <body>
</html>
```
---
## Template inclusão e herança de templates
- **principal.html**:<!-- {li:style="display: inline-block; width:60%;border-right:1px dashed black; padding-right: 10px;font-size:0.8em;"}-->
  ```html
  <html>
    <head>
      <title>Pagina Supimpa - {% block titulo %}{% endblock%}</title>
      <link rel="stylesheet" href="estilos.css">
    </head>
    <body>
      {% include "menu.html" %}
      <main>{% block conteudo %}{% endblock%}</main>
    <body>
  </html>
  ```
  **menu.html:**
  ```html
  <nav><ul><li>Home</li><li>História</li></ul>
  ```
- **home.html**:<!-- {li:style="display: inline-block; width:35%;border-right:1px dashed black; padding-right: 10px;font-size:0.8em;"}-->
  ```html
  {% extends "principal.html" %}
  {% block titulo %}Home{% endblock%}
  {% block conteudo %}
  Conteúdo do Home :D
  {% endblock%}
  ```
  **história.html**:
  ```html
  {% extends "principal.html" %}
  {% block titulo %}Hitória{% endblock%}
  {% block conteudo %}
  História :D
  {% endblock%}
  ```
---
## Sintaxe do template

- Impressão de variáveis no HTML
```html
  <p>Ola! Meu nome é <strong>{{nome}}</strong>!
```

- Usar `.` para acesso a chaves de *dicionário*, indices de listas e atributos de objetos
```html
  {{ my_dict.key }}
  {{ my_object.attribute }}
  {{ my_list.0 }}
```
---
## Sintaxe do template

- Condicionais
```html
{% if athlete_list %}
  Atletas: {{ athlete_list|length }}
{% else %}
  Não há atletas.
{% endif %}
```

- Usar `.` para acesso a chaves de *dicionário*, indices de listas e atributos de objetos
```html
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% empty %}
    <li>Não há atletas cadastrados </li>
{% endfor %}
</ul>
```
[Mais tags e filtros Django](https://docs.djangoproject.com/pt-br/2.1/ref/templates/builtins)

---
## Views

- Views são responsáveis por:
  - Obter e processar a requisição
  - Responder a requisição. Se necessário:
    - Insere/consulta/atualiza/remove instancias
    - Indica o template a ser renderizado

---
<!-- { "slideHash": "urls"} -->
## URLs

- O arquivo `urls.py` indica quais URLs estão disponíveis em um projeto Django
- Altere a lista `urlpatterns` deste arquivo com os endereços desejados

```python
from app_projeto.views import *
from django.views.generic.base import TemplateView
urlpatterns = [
    path('articles/<int:year>/', Post.as_view(),name='articles_per_year'),
    path('', TemplateView.as_view(template_name="home.html"),name='home'),
]
```

- Cada elemento da lista possui um `path` com os parametros: endereço, view e nome
- o nome pode ser referenciado no template para ser gerado a url:
  ```html
  <a href='{% url "home" %}'>Home</a>
  <a href='{% url "articles_per_year" year=2003 %}'>2003 Posts</a>
  ```
---
<!-- {"layout": "2-column-content"} -->
## View - Processamento de uma requisição

```python
from django.shortcuts import render
from django.views import View

class Home(View):
  def get(self, request):
    return render(request,
              "home.html",
              {'sobre': [{"titulo":"De onde eles vêm",
                          "texto":"Lorem ipsum dolor sit amet, consectetur"},
                          {"titulo":"O que eles querem",
                          "texto":"osakdpokasdokaspok"},
                          ]})
  ```
  ```html
  {% for item_sobre in sobre %}
    <h2>{{ item_sobre.titulo}}</h2>
    <p>
      <button class="botao-expandir-retrair">+</button>
      {{item_sobre.texto}}
    </p>
  {% empty %}
    Não <strong>há</strong> sobre ainda :-(
  {% endfor %}
```
---
<!-- { "slideHash": "urls"} -->
## URLs

Para criar a URL, referencie a view criada:

```python
from app_projeto.views import *
from django.views.generic.base import TemplateView
urlpatterns = [
    path('', Home.as_view(),name='home'),
]
```

---
<!-- { "slideHash": "urls-params"} -->
## URLs - Processando URL com parametros



URL:
~ ```python
  urlpatterns = [
      path('diga-ola-para:<str:nome>/<str:cidade>', Ola.as_view(), name='oi'),
      ]
  ```
View:
~  ```python
  class Ola(View):
      def get(self, request, nome,cidade):
          return render(request,
                          "ola.html",
                          {'nome_pessoa': nome,'cidade':cidade})
  ```
Template:
~  ```html
    <p>Ola <strong>{{ nome_pessoa }}</strong> de {{cidade}}!</p>
  ```
Ao acessarmos: `http://127.0.0.1:8000/diga-ola-para:Hasan/BH` será renderizado:

```html
  <p>Ola <strong>Hasan</strong> de BH!</p>
```
---
## Uso de form
- Para usarmos formulários HTMLs, primeiramente podemos criar um formulario como uma classe Python. Por exemplo:
```python
from django import forms
class PessoaForm(forms.Form):
    nome = forms.CharField(label='Nome:', max_length=100)
    data_nascimento = forms.DateField(label="Data Nascimento")
```
- Além de renderizar o HTML, formulários fazem a validação, limpeza/tratamento dos dados

---
## Form - Construtor, atributos e Métodos úteis
- Form(dados,arquivos,initial)
  - dados: dicionário com todos os seus campos e valores
  - arquivos: dicionário que para cada campo que é um arquivo, o ponteiro para o mesmo
  - initial: Dados iniciais (se os dados não forem fornecidos)
- **métodos**
  - `is_valid()`: verifica se o formulário está valido
  - `as_ul()`: renderiza em HTML o form como uma lista
  - `as_p()`: renderiza em HTML o form como usando parágrafos
  - `as_table()`: renderiza em HTML o form como uma table (padrão)
- **atributos**
  - `errors`: dicionário com os erros nos campos preenchidos
  - `cleaned_data`: dicionário com os dados já processados
---
## Form - Exemplo no console
```shell
>>> hasan = PessoaForm({"nome":"","data_nascimento":"oioi"})
>>> hasan.errors
{'nome': ['This field is required.'], 'data_nascimento': ['Enter a valid date.']}
>>> hasan = PessoaForm({"nome":"Daniel Hasan","data_nascimento":"1984-04-14"})
>>> hasan.errors
{}
>>> hasan.is_valid()
True
>>> hasan.cleaned_data
{'nome': 'Daniel Hasan', 'data_nascimento': datetime.date(1984, 4, 14)}
>>> hasan.as_p()
'<p><label for="id_nome">Nome:</label>
    <input type="text" name="nome" value="Daniel Hasan" required id="id_nome" maxlength="100">
  </p>
<p><label for="id_data_nascimento">Data Nascimento:</label>
  <input type="text" name="data_nascimento" value="1984-04-14" required id="id_data_nascimento">
</p>'
```
---
## View - Processamento de uma requisição
<style>
pre{
  max-height: 40vh;
}
</style>
- View:<!-- {li:style="display: inline-block; width:60%;border-right:1px dashed black; padding-right: 10px;font-size:0.8em;"}-->
  ```python
    from django.shortcuts import render
    from django.views import View7
    from datetime import date
    from django import forms
    from django.urls.base import reverse
  class PessoaForm(forms.Form):
      nome = forms.CharField(label='Nome:', max_length=100)
      data_nascimento = forms.DateField(label="Data Nascimento")
    class Contato(View):
      def get(self, request):
        return render(request,
                            "contato.html",
                            {"contato":PessoaForm(initial={"data_nascimento":date.today()})})
      def post(self,request):
        form = PessoaForm(request.POST)
        if form.is_valid():
          # processa o formulario (usando form.cleaned_data)
          return HttpResponseRedirect(reverse('success') )

        return render(request, "contato.html", {'contato': form})
  ```
- Template:<!-- {li:style="display: inline-block; width:35%;padding-right: 10px;font-size:0.8em;"}-->
  ```html
    <h2>Contatos</h2>
    <form method="post">
       {% csrf_token %}
       {{ contato }}
       <button>Enviar</button>
    </form>
  ```

[Formas de exibir o formulário](https://docs.djangoproject.com/en/2.1/ref/forms/api/)


---
<!-- { "slideHash": "model-form"} -->
## Model Form

Considere a classe pessoa:
```python
class Pessoa(models.Model):
  nome = models.CharField(max_length=100)
  data_nascimento = models.DateField()

```

Se desejarmos atualizar dados da pessoa por meio de formulários, usamos o ModelForm:
```python
from django import forms
class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'data_nascimento']
        labels = {"data_nascimento": "Data de Nascimento"}
```
---
## ModelForm - Uso

- Construtor: ModelForm(dados,arquivos,instance)
  - `dados`: Valores que foram preenchidos no formulário
  - `arquivos`: Apontador para os arquivos enviados (opcional)
  - `instance`: Instancia a ser alterada (opcional)

Método save: atualiza/insere a entidade de acordo com os dados passados no construtor

---

## Model Form - exemplo no console (1/2)
```shell
>>> class PessoaForm(forms.ModelForm):
...     class Meta:
...         model = Pessoa
...         fields = ['nome', 'data_nascimento']
...         labels = {"data_nascimento": "Data de Nascimento"}

>>> form = PessoaForm()
>>> form.as_p()
'<p><label for="id_nome">Nome:</label>
    <input type="text" name="nome" required id="id_nome" maxlength="100">
 </p>
 <p><label for="id_data_nascimento">Data de Nascimento:</label>
    <input type="text" name="data_nascimento" required id="id_data_nascimento">
 </p>'
```
---
## Model Form - exemplo no console (2/2)
```shell
>>> from datetime import date
>>> form = PessoaForm({"nome":"Dani","data_nascimento":"1990-04-14"},instance=Pessoa.objects.all()[0])
>>> form.as_p()
'<p><label for="id_nome">Nome:</label>
    <input type="text" name="nome" value="Dani" required id="id_nome" maxlength="100">
 </p>
 <p><label for="id_data_nascimento">Data de Nascimento:</label>
    <input type="text" name="data_nascimento" value="1990-04-14" required id="id_data_nascimento">
  </p>'
>>> form.is_valid()
True
>>> form.save()
<Pessoa: Pessoa object (1)>

```

---
<!-- { "slideHash": "model-form-ex"} -->

## View - Fomulários e modelos:



```python

class SalvarPessoa(View):
    def get(self,request): #Requisitou a exibição do formulário
        return render(request,"salvar_pessoas.html",{"pessoa":PessoaForm()})

    def post(self,request):#via post, salva a pessoa
        form = PessoaForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_pessoas') )
        else:
            return render(request,"salvar_pessoas.html",{"pessoa":form})
```


```html
<h2>Inserir Pessoa</h2>
<form method="post">
   {% csrf_token %}
   {{ pessoa }}
   <button>Enviar</button>
</form>
```
---
## Atualizar elemento

```python
class SalvarTesouro(View):
    def get(self,request,id=None): #Requisitou a exibição do formulário
        pessoa = Pessoa.objects.get(id=id) if id != None else None
        return render(request,"salvar_pessoa.html",{"pessoa":PessoaForm(instance=pessoa)})

    def post(self,request,id=None):#via post, salva a pessoa
        pessoa = Pessoa.objects.get(id=id) if id != None else None
        form = PessoaForm(request.POST,request.FILES, instance=pessoa)

        if form.is_valid():
            form.save()
            #se estiver ok, salva e lista as pessoas
            return HttpResponseRedirect(reverse('lista_pessoas') )
        else:
            #caso nao esteja valido, volte a exibir o formulario
            return render(request,"salvar_pessoas.html",{"pessoa":form})
```

---
<!-- { "slideHash": "static"} -->
## Arquivos estáticos
- Salvamos os arquivos estaticos (imagens, CSS e JS) em uma pasta separada
- Pasta de nome `static`, por padrão, fica dentro a pasta do **app** podendo ser alterada em `settings.py`
- `load static`: Comando para usarmos os endereços estáticos
- `static`: comando/tag Para que seja renderizado um endereço estático
```html
{% load static %}
<html>
  <head>
    <title>Pagina Supimpa - {% block titulo %}{% endblock%}</title>
    <link rel="stylesheet" href="{% static "estilos.css" %}">
  </head>
  <body>
    {% include "menu.html" %}
    <main>{% block conteudo %}{% endblock%}</main>
  <body>
</html>
```
---
## Prática

- **Prática 1**: Exploração Espacial V2
	- Objetivo: treinar criação de templates e entender sua organização e como configurá-lo. [Clique aqui e veja a especificação](https://github.com/daniel-hasan/cefet-web-grad/blob/master/assignments/tasks/template/README.md)
- **Prática 2**: Gerenciamento dos Tesouros do Barba-Ruiva
	- Objetivo:  treinar a criação de visões e templates, acesso ao modelo pela visão [Faça clone deste respositório](https://github.com/daniel-hasan/cefet-web-pirates-django)

---
# Referências

1. https://docs.djangoproject.com
1. https://simpleisbetterthancomplex.com/
1. https://tutorial.djangogirls.org/pt/
