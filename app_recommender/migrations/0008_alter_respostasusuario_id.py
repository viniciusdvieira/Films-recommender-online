# Generated by Django 4.2.5 on 2023-09-30 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_recommender', '0007_alter_respostasusuario_data_resposta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respostasusuario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]