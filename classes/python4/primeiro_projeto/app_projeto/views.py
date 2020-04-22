from django.shortcuts import render
from django.views import View
from .models import Pessoa
from django import forms
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'data_nascimento']
        labels = {"data_nascimento": "Data de Nascimento"}

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
