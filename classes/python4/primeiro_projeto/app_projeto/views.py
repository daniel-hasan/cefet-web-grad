from django.shortcuts import render
from django.views import View
from datetime import date
from django import forms
from django.urls.base import reverse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Pessoa
class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'data_nascimento']
        labels = {"data_nascimento": "Data de Nascimento"}

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


class ListarPessoas(View):
  def get(self,request):
    lst_pessoas = list(Pessoa.objects.all().values("id","nome"))
    return JsonResponse({"pessoas":lst_pessoas})

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
            return HttpResponseRedirect(reverse('home') )
        else:
            #caso nao esteja valido, volte a exibir o formulario
            return render(request,"salvar_pessoa.html",{"pessoa":form})
