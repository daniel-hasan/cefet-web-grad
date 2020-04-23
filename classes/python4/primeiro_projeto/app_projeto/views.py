from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
class Home(View):
    def get(self, request):
        lista_itens = [{"titulo":"De onde eles vêm",
                        "texto":"Lorem ipsum dolor sit amet, consectetur"},
                        {"titulo":"O que eles querem",
                        "texto":"osakdpokasdokaspok"},
                      ]
        itens = {'lista_itens':lista_itens }
        return render(request,"home.html",itens)

class Ola(View):
   def get(self, request, nome,cidade):
       return render(request,
                       "ola.html",
                       {'nome_pessoa': nome,'cidade':cidade})
