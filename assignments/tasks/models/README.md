# cefet-web-music
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

Conforme os [slides](https://daniel-hasan.github.io/cefet-web-grad/classes/python3/#django) crie o projeto `music_project` e, dentro dele, o app `music`. Para que você possa usar este **app** no projeto, entre no `settings.py` e coloque o `music` na lista de `INSTALLED_APPS`.


## Exercício 2 - Criação do Modelo e efetivação das consultas
- Você deverá criar, em `models.py` do app `music` um modelo para armazenar bandas, musicos e estilos musicais. Para isso, você deverá criar as classes (herdades de `model.Model`) **Banda**, **Musico** e **EstiloMusical**. Neste modelo, deverá, para cada classe, armazenar no Banco de Dados o atributo `nome` (i.e. nome da banda, musico e estilo musical).
Faça mais três atributos não textuais (e também que não sejam relacionamentos) para alguma dessas classes. Tais atributos devem ser da sua escolha e fazer sentido no contexto de uma banda/musico e estilo. [Veja os campos aqui](https://docs.djangoproject.com/en/2.1/ref/models/fields/#field-types).

- Tais classes devem ter os seguintes relacionamentos: Para cada **banda** deve ser armazenado seu estilo musical. Cada músico pode ser de mais de uma banda e bandas possuem mais de um músico.

- Crie o método `__str__` para cada uma dessas classes
- Faça o **makemigrations** e **migrate** para atualizar o banco de dados. Como não fizemos alguma configuração prévia, a configuração default é usando o banco de dados SQLLite que armazena os dados em um arquivo (neste caso, foi o arquivo `db.sqlite3`)

- Abra o python usando o ambiente Django deste projeto. Ou seja, use `python3 manage.py shell` na pasta principal do projeto. Você deverá importar todos os modelos para testar usando `from  music.models import *`. Faça os exercícios abaixo e, para **cada um** dos itens abaixo, de um `print` na tela dos comandos/resultados e salve este arquivo no com nome `resultado_X.jpg` em que `X` é o nome do item. Observe que deve-se haver um arquivo por item. **Você deverá entregar o código e os prints no mesmo repositório.**
  - (1) crie algumas instancias de musica e estilos musicais e faça algumas bandas.
    - Cada relacionamento pode ser navegado como se fosse uma consulta, por exemplo, em `Post.objects.all()[0].autores.filter(nome__starts_with="Daniel ")` exibe-se todos os autores em que o primeiro nome é 'Daniel` do primeiro post retornado  
    - Para adicionar elementos em um campo many-to-many use o método `add` do atributo a ser adicionado.
    - Veja o exemplo completo com as classes [dos slides](https://daniel-hasan.github.io/cefet-web-grad/classes/python3/#django):
```shell
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from app_projeto.models import *
>>> from datetime import date
>>> b_assombrado = Blog.objects.create(nome="Blog Assombrado",sobre="Noticias e reportagens sobre o desconhecido")
>>> hasan = Author.objects.create(nome="Daniel Hasan",email="hasan@assombrado.org")
>>> post_forest = Post.objects.create(blog=b_assombrado,
...                             	titulo="Crooked Forest",
...                             	texto="Conheça a enigmática 'Crooked Forest' na Polônia",
...                             	data_publicacao=date(2016, 6, 24),
...                             	rating=4)
>>> post_forest.autores.add(hasan)
>>> Post.objects.all() #exibe todos os Posts para teste
>>> Post.objects.all()[0].autores.all() #para um post especifico, exibe os autores para teste
```
  - (2) exclua e atualize alguns  elementos
  - (3) exiba todas as bandas de um determinado estilo musical. Tal estilo deve ser passado como filtro na consulta.
  - (4)[DESAFIO] Para consulta apresentada em (3), para cada banda, navegue por todos os musicos e imprima seus nomes. Para isso, você deverá usar o conjunto de músicos [veja aqui como fazer](https://docs.djangoproject.com/pt-br/2.1/topics/db/queries/#related-objects).
  - (5) [DESAFIO] Crie o atributo gênero para o músico (feminino ou masculino) e filtre, na consulta 3 apenas bandas que possuem mulheres [veja como fazer consultas por relacionamentos](https://docs.djangoproject.com/pt-br/2.1/topics/db/queries/#lookups-that-span-relationships).
