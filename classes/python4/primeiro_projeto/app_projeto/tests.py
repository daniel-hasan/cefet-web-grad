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

    def test_listar_pessoas(self):
      c = Client()

      #faz a requisição
      str_url = reverse("home")
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
    def test_atualizar(self):
      c = Client()

      #faz a requisição
      id_atualizar = self.pessoas_inseridas[0].id
      str_url = reverse("atualizar",kwargs={"id":id_atualizar})
      c.post(str_url, {"nome":"Daniel","data_nascimento":"2020-01-23"})

      #testes
      lstPessoasCarol = Pessoa.objects.filter(id=id_atualizar,nome="Daniel",
                                            data_nascimento=date(2020,1,23))
      self.assertEquals(1,len(lstPessoasCarol),
                      "Não foi possível encontrar a instancia atualizada")
