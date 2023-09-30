from django.db import models

class RespostasUsuario(models.Model):
    data_resposta = models.DateTimeField(auto_now_add=True, null=True)
    genero_filme_preferido = models.CharField(max_length=255, null=True)
    sentimento_filmes_terror = models.CharField(max_length=255, null=True)
    preferencia_filmes_contemporaneos = models.CharField(max_length=255, null=True)
    protagonista_preferido = models.CharField(max_length=255, null=True)
    final_emocionante_preferido = models.CharField(max_length=255, null=True)
    sentimento_filmes_comedia_romantica = models.CharField(max_length=255, null=True)
    diretor_favorito = models.CharField(max_length=255, null=True)
    gosto_filmes_acao_adrenalina = models.CharField(max_length=255, null=True)
    ator_atriz_favorito = models.CharField(max_length=255, null=True)
    preferencia_filmes_fatos_reais_ficcao = models.CharField(max_length=255, null=True)
    recomendacao_filme = models.TextField()

    def __str__(self):
        return f"Resposta de {self.data_resposta}"
