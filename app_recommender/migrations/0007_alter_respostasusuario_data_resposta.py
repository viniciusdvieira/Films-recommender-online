# Generated by Django 4.2.5 on 2023-09-30 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_recommender', '0006_respostasusuario_ator_atriz_favorito_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respostasusuario',
            name='data_resposta',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
