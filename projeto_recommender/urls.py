
from django.urls import path
from app_recommender import views
from app_recommender.views import proxy_image

urlpatterns = [
    #rota, view responsavel, nome de referencia
    path('',views.home,name='home'),

    path('respostas/', views.recomendacao_filmes, name='recomendation'),

    path('proxy_image/<path:image_url>/', proxy_image, name='proxy_image'),

    
]
