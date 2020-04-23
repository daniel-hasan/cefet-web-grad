<!-- {"layout": "title"} -->
# Django - Renderização de<br> Páginas Web
## Templates, Views, arquivos estáticos e URLs
---
## Principais Componentes  Django

- **Template**: Exibição do html (usualmente, dinâmico)
- **View**: Tratamento da requisição, elaboração da resposa, geralmente, por meio da renderização  de um **template**. Se necessário, consultando o banco de dados pelos **models**
- **Models**: Responsável pela persistência/gerenciamento dos dados

---
## Relação Entre os Componentes
::: figure .figure-slides.clean
![Componentes - Requisição é tratada pela urls.py](../../images/django-funcionamento-1.png) <!-- {.bullet.figure-step.bullet-no-anim} -->
![A urls.py invoca a View para criar a resposta](../../images/django-funcionamento-2.png) <!-- {.bullet.figure-step.bullet-no-anim} -->
![Eventualmente, essa resposta pode precisar de obter algo no banco](../../images/django-funcionamento-3.png) <!-- {.bullet.figure-step.bullet-no-anim} -->
![Pode ser gerado um template para a resposta](../../images/django-funcionamento-4.png) <!-- {.bullet.figure-step.bullet-no-anim} -->
![A resposta é gerada para o usuário](../../images/django-funcionamento-5.png) <!-- {.bullet.figure-step.bullet-no-anim} -->
![A resposta é gerada para o usuário](../../images/django-funcionamento-5.png) <!-- {.bullet.figure-step.bullet-no-anim} -->
:::

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
## Templates - Exemplo no Jupyter

```python
from django.template import engines
django_engine = engines['django']
template = django_engine.from_string("Ola {{ name }}!")
dado = {'name':'Hasan'}
template.render(dado)
```

:::result

Ola Hasan!

:::

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
- [Veja opções do atributo **options** aqui](https://docs.djangoproject.com/en/3.1/topics/templates/#django.template.backends.django.DjangoTemplates)

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
<!-- { "slideHash": "urls"} -->
## URLs

- O arquivo `urls.py` indica quais URLs estão disponíveis em um projeto Django
- Altere a lista `urlpatterns` deste arquivo com os endereços desejados

```python
from app_projeto.views import *
from django.views.generic.base import TemplateView
urlpatterns = [
    path('servicos', TemplateView.as_view(template_name="servicos.html"),name='home'),
    path('', TemplateView.as_view(template_name="home.html"),name='home'),
]
```

- Cada elemento da lista possui um `path` com os parametros: endereço, view e nome
- o nome pode ser referenciado no template para ser gerado a url:
  ```html
  <a href='{% url "home" %}'>Home</a>
  <a href='{% url "servicos" %}'>Serviços</a>
  ```

---
## Sintaxe do template

- Impressão de variáveis no HTML
  ```html
    <p>Ola! Meu nome é <strong>{{nome}}</strong>!</p>
  ```

---
## Sintaxe do Template

- Use `.` para acessar itens no dicionário
```python
from django.template import engines
django_engine = engines['django']
dados_pagina = {
                   "cliente":{
                     "nome":"Alice",
                     "endereco":{"rua":"A","numero":2010,
                                 "bairro":"Esperança","Cidade":"Belo Horizonte",
                                 "Estado":"MG"
                                 },
                      "telefones":["(31) 555-4444","(31) 999-4444"]
                   }
                }
template = django_engine.from_string("Ola {{ cliente.nome }}! Telefone: {{cliente.telefones.0}}")
template.render(dados_pagina)
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

- Estrutura de Repetição
```html
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% empty %}
    <li>Não há atletas cadastrados </li>
{% endfor %}
</ul>
```
[Mais tags e filtros Django](https://docs.djangoproject.com/pt-br/3.0/ref/templates/builtins)

---
## Views

- Views são responsáveis por:
  - Obter e processar a requisição
  - Responder a requisição. Se necessário:
    - Insere/consulta/atualiza/remove instancias
    - Indica o template a ser renderizado


---
<!-- {"layout": "2-column-content"} -->
## View - Processamento de uma requisição

```python
from django.shortcuts import render
from django.views import View

class Home(View):
    def get(self, request):
        lista_itens = [{"titulo":"De onde eles vêm",
                        "texto":"Lorem ipsum dolor sit amet, consectetur"},
                        {"titulo":"O que eles querem",
                        "texto":"osakdpokasdokaspok"},
                      ]
        itens = {'lista_itens':lista_itens }
        return render(request,"home.html",itens)
```

```html
  {% for item_sobre in lista_itens %}
    <li><strong>{{ item_sobre.titulo}}:</strong>
                  {{item_sobre.texto}}
    </li>
  {% empty %}
    Não <strong>há</strong> sobre ainda :-(
  {% endfor %}
```
---
<!-- { "slideHash": "urls-views"} -->
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
---
<!-- { "slideHash": "urls-params"} -->
## URLs - Referenciando a URL com parametros no template



URL:
~ ```python
  urlpatterns = [
      path('/', TemplateView.as_view(template_name="pessoas_ola.html"), name='pessoas'),
      path('diga-ola-para:<str:nome>/<str:cidade>', Ola.as_view(), name='oi'),
      ]
  ```
Template:
~  ```html
    <a href='{% url "oi" nome="Hasan" cidade="BH" %}'>Hasan</a>
    <a href='{% url "oi" nome="Alice" cidade="Contagem" %}'>Alice</a>
    <a href='{% url "oi" nome="Bob" cidade="São Paulo" %}'>Bob</a>
  ```
Ao acessarmos: `http://127.0.0.1:8000/diga-ola-para:Hasan/BH` será renderizado:

```html
<a href='diga-ola-para:Hasan/BH'>Hasan</a>
<a href='diga-ola-para:Alice/Contagem'>Alice</a>
<a href='diga-ola-para:Bob/São Paulo'>Bob</a>
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
# Prática 1 - Exploração Espacial


Objetivo: treinar criação de templates e entender sua organização e como configurá-lo. [Clique aqui e veja a especificação](https://github.com/daniel-hasan/cefet-web-grad/blob/master/assignments/tasks/template/README.md)


---
# Referências

1. https://docs.djangoproject.com
1. https://simpleisbetterthancomplex.com/
1. https://tutorial.djangogirls.org/pt/
