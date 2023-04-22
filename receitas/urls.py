from django.urls import path
from . import views

urlpatterns = [
    path('', views.receitas, name='receitas'),
    path('cadastro_receitas/', views.cadastro_receitas, name='cadastro_receitas'),
    path('edit_receitas/<int:id>', views.edit_receitas, name='edit_receitas'),
]
