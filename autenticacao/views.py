from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate

# Create your views here.

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        
        user.save()
        return HttpResponse('Usuário cadastrado com sucesso!')
    
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        
        user = authenticate(username=nome, password=senha)
        if user is not None:
            auth_login(request, user)
            return render(request, 'base.html')
        else:
            
            return HttpResponse('Usuário não encontrado!')
    
