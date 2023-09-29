from django.db import models

class RespostaUsuario(models.Model):
    usuario = models.AutoField(primary_key=True)
    pergunta = models.CharField(max_length=255)
    resposta = models.CharField(max_length=255)
    data_resposta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resposta de Usuário {self.usuario} - Pergunta: {self.pergunta}"
