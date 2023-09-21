
from django.urls import path
from app_recommender import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    path('',views.home,name='home'),

    path('respostas/', views.recomendacao_filmes, name='recomendation'),

        # Rota para a página index2
    path('index2/', views.index2, name='index2'),

    
]
