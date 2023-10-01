# Generated by Django 4.2.5 on 2023-09-30 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_recommender', '0005_alter_respostasusuario_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='respostasusuario',
            name='ator_atriz_favorito',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='respostasusuario',
            name='diretor_favorito',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='respostasusuario',
            name='final_emocionante_preferido',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='respostasusuario',
            name='genero_filme_preferido',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='respostasusuario',
            name='gosto_filmes_acao_adrenalina',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='respostasusuario',
            name='preferencia_filmes_contemporaneos',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='respostasusuario',
            name='preferencia_filmes_fatos_reais_ficcao',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='respostasusuario',
            name='protagonista_preferido',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='respostasusuario',
            name='sentimento_filmes_comedia_romantica',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='respostasusuario',
            name='sentimento_filmes_terror',
            field=models.CharField(max_length=255, null=True),
        ),
    ]