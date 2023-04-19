from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        
        user.save()
        return HttpResponse('Usuário cadastrado com sucesso!')
    
def login(request):
    return HttpResponse('Login')
