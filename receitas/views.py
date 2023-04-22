from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from . models import Receitas
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
def receitas(request):
    if request.method == 'GET':
        receitas = Receitas.objects.all()
        return render(request, 'receitas.html', {'receitas': receitas})

@login_required
def cadastro_receitas(request):
    if request.method == 'GET':
        nome_prato = request.GET.get('nome_prato')
        print(nome_prato)
        
        return render(request, 'cadastro_receitas.html')
    elif request.method == 'POST':
        nome_prato = request.POST.get('nome_prato')
        categoria = request.POST.get('categoria')
        ingredientes = request.POST.get('ingredientes')
        preco0 = request.POST.get('preco0')
        preco1 = request.POST.get('preco1')
        preco2 = request.POST.get('preco2')
        foto_prato = request.FILES.get('foto_prato')
        
        receitas = Receitas(
            criador=request.user,
            nome_prato=nome_prato,
            categoria=categoria,
            ingredientes=ingredientes,
            preco0=preco0,
            preco1=preco1,
            preco2=preco2,
            foto_prato=foto_prato,
        )
        receitas.save()
        
        messages.add_message(request, messages.SUCCESS, 'Receita cadastrada com sucesso!')
        return redirect(reverse('cadastro_receitas'))
    
def edit_receitas(request, id):
        id = request.GET.get('id')
        print(id)
        return HttpResponse(id)