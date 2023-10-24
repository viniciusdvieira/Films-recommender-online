
from django.urls import path
from app_recommender import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    path('',views.home,name='home'),

    path('respostas/', views.recomendacao_filmes, name='recomendation'),



    
]
