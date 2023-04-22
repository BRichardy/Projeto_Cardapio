from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Receitas(models.Model):
    criador = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    categoria = models.CharField(max_length=100)
    nome_prato = models.CharField(max_length=100)
    ingredientes = models.TextField()
    preco0 = models.FloatField()
    preco1 = models.FloatField(default=None)
    preco2 = models.FloatField(default=None)
    foto_prato = models.ImageField(upload_to="logos")
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.nome_prato