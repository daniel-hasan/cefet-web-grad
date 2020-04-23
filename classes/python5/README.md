<!-- {"layout": "title"} -->
# Django - Salvar dados e Finalização de uma Aplicação
## Forms, ModelForms, Testes Unitários e Ajax
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
  - `cleaned_data`: dicionário com os dados já processados. Só existe após executarmos `is_valid`
---
## Form - Exemplo no Jupyter
```python
teste_1 = PessoaForm({"nome":"","data_nascimento":"oioi"})
print(f"Erros 1: {teste_1.errors} is valid? {hasan.is_valid()}")

teste_2 = PessoaForm({"nome":"Daniel Hasan","data_nascimento":"1984-04-14"})
print(f"Erros 2: {hasan.errors} is valid? {hasan.is_valid()}")

print("Cleaned_data: {hasan.cleaned_data}")

print()
''
```
:::result
Erros 1: {'nome': ['This field is required.'], 'data_nascimento': ['Enter a valid date.']} is valid? False<br>
Erros 2: {} is valid? True<br>
Cleaned_data: {'nome': 'Daniel Hasan', 'data_nascimento': datetime.date(1987, 3, 2)}
:::
---
## Form - exemplo no Jupyter (continuação) - as_p
```python
print(teste_2.as_p())
```
Resultado:
```html
<p><label for="id_nome">Nome:</label>
    <input type="text" name="nome" value="Daniel Hasan" required id="id_nome" maxlength="100">
  </p>
<p><label for="id_data_nascimento">Data Nascimento:</label>
  <input type="text" name="data_nascimento" value="1984-04-14" required id="id_data_nascimento">
</p>
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
  from django.views import View
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

[Formas de exibir o formulário](https://docs.djangoproject.com/en/3.0/ref/forms/api/)


---
<!-- { "slideHash": "model-form"} -->
## Model Form

Considere a classe pessoa:
```python
class Pessoa(models.Model):
  nome = models.CharField(max_length=100)
  data_nascimento = models.DateField()
  def __str__(self):
      return f"{self.nome} - {self.data_nascimento}"

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
## Model Form - exemplo no Jupyter - form vazio
```python
form = PessoaForm()
print(form.as_p())

```
Resultado:
```html
<p>
  <label for="id_nome">Nome:</label>
  <input type="text" name="nome" required id="id_nome" maxlength="100">
</p>
<p>
  <label for="id_data_nascimento">Data de Nascimento:</label>
  <input type="text" name="data_nascimento" required id="id_data_nascimento">
</p>
```
---
## Model Form - exemplo no Jupyter - inserção
```python
dados_recebidos = {"nome":"Hasan","data_nascimento":"1990-02-20"}
form = PessoaForm(dados_recebidos)
print(form.as_p())
if form.is_valid():
  form.save()
hasan = form.instance
```
Resultado:
```html
<p>
  <label for="id_nome">Nome:</label>
  <input type="text" name="nome" value="Hasan" required id="id_nome" maxlength="100">
</p>
<p>
  <label for="id_data_nascimento">Data de Nascimento:</label>
  <input type="text" name="data_nascimento" value="1990-02-20" required id="id_data_nascimento">
</p>
```
---
## Model Form - exemplo no Jupyter (2/2)
```python
dados_recebidos = {"nome":"Hasan Dalip","data_nascimento":"1970-02-20"}
form = PessoaForm(dados_recebidos,instance=hasan)
if form.is_valid():
    form.save()
print(form.as_ul())
```
Resultado:
```html
<p>
  <label for="id_nome">Nome:</label>
  <input type="text" name="nome" value="Dani" required id="id_nome" maxlength="100">
</p>
<p>
  <label for="id_data_nascimento">Data de Nascimento:</label>
  <input type="text" name="data_nascimento" value="1970-02-20" required id="id_data_nascimento">
</p>
```

---
<!-- { "slideHash": "model-form-ex"} -->
## Exemplo de inserção/listagem com ModelForm

<style>
p{
    line-height:1;
    margin: 0px;
}
</style>

- urls.py:<!-- {li:style="display: inline-block; width:45%;border-right:1px dashed black; padding-right: 10px;font-size:0.8em;"}-->
  ```python
  urlpatterns = [
      path('pessoa/insere', SalvarPessoa.as_view(), name='inserir'),
      path('', ListarPessoas.as_view(), name='lista_pessoas'),
      ]
  ```
  View:
  ```python
  from django.http import HttpResponseRedirect
  from django.url import reverse
  class ListarPessoas(View):
    def get(self,request):
      lst_pessoas = Pessoa.objects.all().values("id","nome")
      return render(request,"listar_pessoas.html",{"pessoas":lst_pessoas})
  class SalvarPessoa(View):
      def get(self,request): #Requisitou a exibição do formulário
          return render(request,"salvar_pessoa.html",{"pessoa":PessoaForm()})

      def post(self,request):#via post, salva a pessoa
          form = PessoaForm(request.POST,request.FILES)

          if form.is_valid():
              form.save()
              return HttpResponseRedirect(reverse('listar_pessoas') )
          else:
              return render(request,"salvar_pessoa.html",{"pessoa":form})
  ```

- listar_pessoas.html:<!-- {li:style="display: inline-block; width:50%;font-size:0.8em;position:relative;top:-3em;"}-->
  ```html
  <ul>
      {% for pessoa in pessoas %}
        <li>{{pessoa.nome}}</li>
      {% endfor %}
  </ul>
  ```

  salvar_pessoas.html:
  ```html
  <h2>Salvar Pessoa</h2>
  <form method="post">
     {% csrf_token %}
     {{ pessoa }}
     <button>Enviar</button>
  </form>
  ```

---
<!-- { "slideHash": "model-form-ex"} -->
## Exemplo de atualização com ModelForm

<style>
p{
    line-height:1;
    margin: 0px;
}
</style>

- urls:<!-- {li:style="display: inline-block; width:45%;border-right:1px dashed black; padding-right: 10px;font-size:0.8em;"}-->
  ```python
  urlpatterns = [
      path('pessoa/<int:id>', SalvarPessoa.as_view(),name='atualizar'),
      path('pessoa/insere', SalvarPessoa.as_view(), name='inserir'),
      path('', ListarPessoas.as_view(), name='listar_pessoas'),
      ]
  ```
  View:
  ```python
  from django.http import HttpResponseRedirect
  from django.url import reverse
  class ListarPessoas(View):
    def get(self,request):
      lst_pessoas = Pessoa.objects.all().values("id","nome")
      return render(request,"listar_pessoas.html",{"pessoas":lst_pessoas})

  class SalvarPessoa(View):
      def get(self,request,id=None): #Requisitou a exibição do formulário
          pessoa = Pessoa.objects.get(id=id) if id != None else None
          return render(request,"salvar_pessoa.html",{"pessoa":PessoaForm(instance=pessoa)})

      def post(self,request,id=None):#via post, salva a pessoa
          pessoa = Pessoa.objects.get(id=id) if id != None else None
          form = PessoaForm(request.POST,request.FILES, instance=pessoa)

          if form.is_valid():
              form.save()
              #se estiver ok, salva e lista as pessoas
              return HttpResponseRedirect(reverse('listar_pessoas') )
          else:
              #caso nao esteja valido, volte a exibir o formulario
              return render(request,"salvar_pessoa.html",{"pessoa":form})
  ```

- listar_pessoas.html:<!-- {li:style="display: inline-block; width:50%;font-size:0.8em;position:relative;top:-3em;"}-->
  ```html
  <ul>
      {% for pessoa in pessoas %}
        <li><a href="{% url "atualizar" pessoa.id %}">{{pessoa.nome}}</a></li>
      {% endfor %}
  </ul>
  ```

  salvar_pessoas.html:
  ```html
  <h2>Salvar Pessoa</h2>
  <form method="post">
     {% csrf_token %}
     {{ pessoa }}
     <button>Enviar</button>
  </form>
  ```
---
## Práticas

- **Prática 1**: Gerenciamento dos Tesouros do Barba-Ruiva
	- Objetivo:  treinar a criação de visões e templates, acesso ao modelo pela visão [Veja a especificação aqui](https://github.com/daniel-hasan/cefet-web-pirates-django). Este GitHub possui o código inicial. Para fazer esta implementação, faça download deste repositório (ou faça um fork).

- **Prática 2**: Há uma forma ainda mais simples para trabalhar com requisições Web usando Django! [Siga as instruções aqui](https://github.com/daniel-hasan/cefet-web-pirates-django-generic) para usar [Generic Views](https://docs.djangoproject.com/pt-br/3.0/topics/class-based-views/generic-editing/#model-forms) e deixar o código ainda mais lindão e simples :). Neste exemplo, você poderá também trabalhar com autenticação de usuário.
---
## Testes unitários

- Testes automatizados são uma boa prática de programação:
  - Simples verificação
  - Pode-se usar ferramentas como o [bitbucket Pipelines](https://confluence.atlassian.com/bitbucket/get-started-with-bitbucket-pipelines-792298921.html) para sempre verificar estes testes.
- É possível, dentre outras possibilidades, simular requisições e autenticações
- [Veja documentação](https://docs.djangoproject.com/en/3.0/topics/testing/tools/)
---
## Testes unitários - Modo de Uso

- Cria-se uma classe de teste era será subclasse de `TestCase` do módulo `django.test.testcases`
- Nessa classe, cria-se os métodos de teste com prefixo `test` e, se necessário, o método `setUp` para sua inicialização
- Use o método get ou post da classe `Client` (módulo `django.test.client`) para simular uma requisição
- Ao longo do código, use os méotodos `assert*` para verificar a corretude da execução.
  - Caso haja algum erro, é lançado uma exceção
  - [Veja a lista de possíveis asserts](https://docs.python.org/3/library/unittest.html#assert-methods)
---
## Exemplo
```python
#imports omitidos
class TestStudent(TestCase):
    def setUp(self):
      #cria usuario para posterior autenticação
      self.senha_autenticacao = "12345"
      self.my_admin = User.objects.create_superuser('myuser', 'myemail@test.com',
                                                          self.senha_autenticacao)

    def test_obtem_aluno(self):
      resposta = c.get("obtem_aluno/102")

      #realiza autenticação
      c.login(username=self.my_admin.username, password=self.senha_autenticacao)

      #verifica se o código http de resposta foi 200 (OK)
      self.assertEqual(response.status_code, 200)

      #o atributo context possui o dado da resposta
      dados_resposta = resposta.context

      #verifica algum dado da resposta
      self.assertTrue("nome" in dados_resposta, "Não foi retornado o nome do aluno")
```
---
## Testes unitários - Funcionamento

- Para garantir independencia entre testes, quando o teste é executado, é criado uma base de dados nova  e, para cada método de teste é executado nesta ordem:
  - `setUp` (se existir)
  - o método de teste
  - `tearDown` (se existir)
  - Os dados da base de teste são completamente removidos - para este teste não afetar os demais

---
## Teste unitário em nosso exemplo - Inicialização

```python
from django.test.client import Client
from django.test.testcases import TestCase
from .models import Pessoa
from .views import ListarPessoas, SalvarPessoa
from datetime import date
from django.urls import reverse

class TestPessoaViews(TestCase):

    def setUp(self):
        self.pessoas_inseridas = []
        self.pessoas_inseridas.append(Pessoa.objects.create(nome="Alice", data_nascimento= date(2020,1,20)))
        self.pessoas_inseridas.append(Pessoa.objects.create(nome="Bob", data_nascimento=date(2019,2,19)))

```
---
## Teste unitário em nosso exemplo - Teste de Listar pessoas

```python
class TestPessoaViews(TestCase):
  def test_listar_pessoas(self):
      c = Client()

      #faz a requisição
      str_url = reverse("listar_pessoas")
      resposta = c.get(str_url)

      #obtem dados da resposta
      dados_resposta = resposta.context

      #realiza o teste - se a lista de pessoas inserida é igual à obtida pela resposta
      lst_pessoas_resposta = dados_resposta["pessoas"]

      for pessoa_resposta in lst_pessoas_resposta:
          #procura pessoa no pessoas_inseridas
          encontrou = False
          for pessoa_inserida in self.pessoas_inseridas:
              if pessoa_resposta["id"] == pessoa_inserida.id:
                  encontrou = True
                  self.assertEqual(pessoa_resposta["nome"],pessoa_inserida.nome,"Nome inesperado ao listar pessoas")
          self.assertTrue(encontrou, f"A pessoa {pessoa_resposta} não foi encontrada")
      self.assertEqual(len(self.pessoas_inseridas),len(lst_pessoas_resposta),
                      "O número de pessoas inseridas é diferente do obtido na resposta!")
```
---
## Teste unitário em nosso exemplo - Teste de inserção

```python
class TestPessoaViews(TestCase):
  def test_inserir(self):
      c = Client()

      #faz a requisição
      str_url = reverse("inserir")
      c.post(str_url, {"nome":"Carol","data_nascimento":"2020-02-01"})

      #testes
      lstPessoasCarol = Pessoa.objects.filter(nome="Carol",
                                              data_nascimento=date(2020,2,1))
      self.assertNotEquals(0,len(lstPessoasCarol),
                      "Não foi possível encontrar a instancia inserida")
      self.assertEquals(1,len(lstPessoasCarol),
              "A instancia foi inserida mais de uma vez")
```
---
## Teste unitário em nosso exemplo - Teste de atualização

```python
class TestPessoaViews(TestCase):
  def test_atualizar(self):
      c = Client()

      #faz a requisição
      id_atualizar = self.pessoas_inseridas[0].id
      str_url = reverse("atualizar",kwargs={"id":id_atualizar})
      c.post(str_url, {"nome":"Daniel","data_nascimento":"2020-01-23"})

      #testes
      lstPessoasCarol = Pessoa.objects.filter(id=id_atualizar)
      self.assertEquals(1,len(lstPessoasCarol),
                      "Não foi possível encontrar a instancia atualizada")

```
---
## Respostas via Ajax (1/2)
- Ajax é usado no front-end para requisições assincronas
  - Se necessário, veja aula Ajax: [slides](https://fegemo.github.io/cefet-front-end/classes/js7/)/[vídeo-aula](https://www.youtube.com/watch?v=STXnmGs3wuA&list=PLNaBD3CnN0-8b7lNxYp5GP_uajyFRn2ek&index=102)
- Resposta **apenas** em JSON
  ```python
  from django.http import HttpResponseRedirect, JsonResponse
  from django.url import reverse

  class ListarPessoas(View):
    def get(self,request):
      lst_pessoas = list(Pessoa.objects.all().values("id","nome"))
      return JsonResponse({"pessoas":lst_pessoas})

  ```
---
## Respostas via Ajax (2/2)
- Resposta em JSON caso seja uma requisição Ajax
  ```python
  from django.http import HttpResponseRedirect
  from django.url import reverse

  class ListarPessoas(View):
    def get(self,request):
      lst_pessoas = list(Pessoa.objects.all().values("id","nome"))
      if request.is_ajax():
        return render(request,"listar_pessoas.html",{"pessoas":lst_pessoas})
      else:
        return JsonResponse({"pessoas":lst_pessoas})
  ```

- Para aplicações que façam um grande uso dessas requisições, considerar usar a API Rest: [Veja documentação](https://www.django-rest-framework.org/), [Veja um exemplo](https://medium.com/@marcosrabaioli/criando-uma-api-rest-utilizando-django-rest-framework-parte-1-55ac3e394fa)
  - Nele, é possivel implementar inclusive autenticação para requisições deste tipo ([ver exemplo](https://medium.com/@marcosrabaioli/django-rest-framework-e-django-oauth-toolkit-c71f8920db08))

---
# Prática 3

Por fim, faça testes unitários na Prática 2 para as operações de busca, atualização, remoção e inserção dos dados. Além disso, use Ajax para obter a lista de tesouros e remover um tesouro.
---
# Referências

1. https://docs.djangoproject.com
1. https://simpleisbetterthancomplex.com/
1. https://tutorial.djangogirls.org/pt/
