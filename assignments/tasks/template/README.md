# cefet-web-space
Use o Linux para este tutorial.

## Instalação do ambiente



- Verifique se o Python 3> está instalado. Digite `python3`. Caso não funcione, tente `python` e veja se a versão é >=3.0:
```shell
hasanzim@maquina:~$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

- Caso não esteja, digite `sudo apt-get install python3 python3-pip`. O python3-pip é um instalador de pacotes/bibliotecas do python.

- Tente importar o módulo django:
```shell
hasanzim@maquina:~$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>import django
```


Caso não funcione, instale-o usando o comando  `pip`. **Não é recomendável usar `sudo` para este comando**.
```
pip install django
```
- Caso você tenha o python 2.X instalado na máquina, você deverá usar o comando como `pip3` ao invés de `pip`.

## Exercício1 - Configuração do projeto

Conforme os [slides](https://daniel-hasan.github.io/cefet-web-grad/classes/python3/#django) crie o projeto `exploracao_espacial` e, dentro dele, o app `space`. Para que você possa usar este **app** no projeto, entre no `settings.py` e coloque o nome do app (i.e. `space`) na lista de `INSTALLED_APPS`.

**Não é recomendável usar `sudo` para configurar o projeto**.
## Exercício 2 - Separação do código em templates

Abra o arquivo [`cefet-web-space.zip`](../cefet-web-space.zip). Este arquivo possui o html estatico do blog. Você deverá separar a parte que se repete da parte específica de cada arquivo usando templates Django. Para isso
crie uma pasta `templates` dentro do projeto. Dentro dela, crie os seguintes HTMLs:

  - `base.html`: irá conter o menu a tag main **apenas** com um bloco que será alterada de acordo com qual página será aberta no menu

  - `home.html` e `philae.html`: ambas herdarão de `base.html`. Você deverá sobrepor o bloco criado em `base.html` colocando o conteúdo que estaria na tag `main` em cada uma dessas páginas.

Para que os seus templates forem encontrados, configure em `settings.py` a propriedade `DIRS` com o nome da pasta criada:
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            # ... some options here ...
        },
    },
]
```

## Exercício 3 - Configuração da URL e do Menu

Para testar, configure as URLs (no arquivo `urls.py`) associando à sua respectiva view. Você pode associar à view de duas formas: usando a view já criada [TemplateView](https://daniel-hasan.github.io/cefet-web-grad/classes/python4/#urls) ou criando uma view `views.py`. Você deverá criar duas URLs para:

- (1) ao acessar a raiz `/` do site, deverá ser apresentado o `home.html`;
- (2) ao acessar `/sobre-philiae`, deverá ser apresentado o `philiae.html`.

Logo após, no menu, para cada link, você gerar a url pelo seu nome ([ver slides](https://daniel-hasan.github.io/cefet-web/classes/python4/#urls)) .


Rode o blog usando `python3 manage.py runserver` e acesse o site.
Por enquanto, você ainda verá o site desformatado, sem imagens, CSS e JavaScript. No próximo exercício você incluirá esses elementos.


## Exercício 4 - Arquivos estáticos

Agora, crie uma pasta `static` **dentro da pasta do app** inclua os CSS e JS lá.  Logo após:

- Referencie o endereço CSS na tag HEAD de `base.html` usando  os comandos apropriados para gerar a URL estática do CSS ([ver slides](https://daniel-hasan.github.io/cefet-web/classes/python4/#static))

- Referencie apropriadamente códigos JavaScript: (1) `home.js` em  `base.html`; e (2) `philiae.js` em `philiae.html`. Não deixe de usar os comandos apropriados para gerar a URL deste recurso estático ao referenciá-los.

- Dentro da pasta estática, crie uma pasta `img` para armazenar todas as imagens. Referencie as imagens nos arquivos HTMLs apropriadamente.

Note que você não precisará fazer nada com as URLs externas.
