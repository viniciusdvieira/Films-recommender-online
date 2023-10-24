from django.db import models

class RespostasUsuario(models.Model):
    data_resposta = models.DateTimeField(auto_now_add=True, null=True)
    pergunta1 = models.CharField(max_length=255, null=True)
    pergunta2 = models.CharField(max_length=255, null=True)
    pergunta3 = models.CharField(max_length=255, null=True)
    pergunta4 = models.CharField(max_length=255, null=True)
    pergunta5 = models.CharField(max_length=255, null=True)
    pergunta6 = models.CharField(max_length=255, null=True)
    pergunta7 = models.CharField(max_length=255, null=True)
    pergunta8 = models.CharField(max_length=255, null=True)
    pergunta9 = models.CharField(max_length=255, null=True)
    pergunta10 = models.CharField(max_length=255, null=True)
    recomendacao_filme = models.TextField()

    def __str__(self):
        return f"Resposta de {self.data_resposta}"
    

class FilmePesquisado(models.Model):
    nome_filme = models.CharField(max_length=255)
    data_pesquisa = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_filme
