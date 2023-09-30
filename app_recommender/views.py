
from django.shortcuts import render, redirect
from .forms import PerguntasForm
from config import API_KEY 
import requests
from .models import RespostasUsuario
from django.http import JsonResponse


def home(request):
    return render(request,'src/index.html')

def index2(request):
    return render(request, 'respostas/index2.html')

def obter_recomendacao_filme(respostas):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_modelo = "gpt-3.5-turbo"

    
    mapeamento_respostas = {
        'q1': {'a': 'Ação', 'b': 'Comédia', 'c': 'Drama', 'd': 'Ficção Científica', 'e': 'Romance'},
        'q2': {'a': 'Adoro!', 'b': 'Gosto de vez em quando.', 'c': 'Não me importo.', 'd': 'Não gosto muito.', 'e': 'Odeio!'},
        'q3': {'a': 'Clássicos', 'b': 'Contemporâneos', 'c': 'Não tenho preferência.', 'd': 'Depende do filme.', 'e': 'Não assisto muitos filmes.'},
        'q4': {'a': 'Masculino', 'b': 'Feminino', 'c': 'Não tenho preferência.', 'd': 'Dupla masculina/feminina', 'e': 'Outro (especifique)'},
        'q5': {'a': 'Final Feliz', 'b': 'Final Surpreendente', 'c': 'Final Aberto', 'd': 'Final Triste', 'e': 'Não tenho preferência.'},
        'q6': {'a': 'Amo!', 'b': 'Gosto de vez em quando.', 'c': 'Não me importo.', 'd': 'Não gosto muito.', 'e': 'Não suporto!'},
        'q7': {'a': 'Christopher Nolan', 'b': 'Quentin Tarantino', 'c': 'Martin Scorsese', 'd': 'Greta Gerwig', 'e': 'Não tenho preferencia'},
        'q8': {'a': 'Sim, adoro!', 'b': 'Sim, gosto.', 'c': 'Não me importo.', 'd': 'Não muito.', 'e': 'Não suporto.'},
        'q9': {'a': 'Tom Hanks', 'b': 'Meryl Streep', 'c': 'Leonardo DiCaprio', 'd': 'Scarlett Johansson', 'e': 'Não tenho preferencia'},
        'q10': {'a': 'Baseados em fatos reais', 'b': 'Pura ficção', 'c': 'Não tenho preferência.', 'd': 'Depende do filme.', 'e': 'Não assisto muitos filmes.'},
    }

    
    perguntas = [
        "Qual é o seu gênero de filme preferido?",
        "Como você se sente sobre filmes de terror?",
        "Prefere filmes clássicos ou contemporâneos?",
        "Qual tipo de protagonista você prefere?",
        "Qual final de filme você acha mais emocionante?",
        "Como você se sente sobre filmes de comédia romântica?",
        "Qual é o seu diretor de filmes favorito?",
        "Você gosta de filmes de ação com muita adrenalina?",
        "Qual é o seu ator ou atriz favorito(a)?",
        "Você prefere filmes baseados em fatos reais ou pura ficção?"
    ]

    # Depurar e verificar as perguntas e respostas
    print("Perguntas e respostas recebidas:")
    mensagens_formatadas = []
    for idx, (pergunta, resposta) in enumerate(zip(perguntas, respostas.values())):
        pergunta_formatada = f"{pergunta} {mapeamento_respostas[f'q{idx + 1}'][resposta]}"
        mensagens_formatadas.append(pergunta_formatada)
        print(f"Pergunta {idx + 1}: {pergunta_formatada}")

    # Montar as mensagens com perguntas e respostas formatadas
    mensagens = []
    for pergunta_formatada in mensagens_formatadas:
        mensagem_pergunta = {"role": "user", "content": pergunta_formatada}
        mensagens.extend([mensagem_pergunta])

    mensagem_final = [
        {"role": "assistant", "content": "Recomende um filme com base nas seguintes respostas:"},
        {"role": "system", "content": "Você é um assistente de recomendação de filmes. Não utilize informações anteriores dessa conversa para recomendar um novo filme"}
    ]

    mensagens.extend(mensagem_final)
    
    body_mensagem = {
        "model": id_modelo,
        "messages": mensagens
    }

    response = requests.post(link, headers=headers, json=body_mensagem)

    if response.status_code == 200:
        resposta_json = response.json()
        mensagem = resposta_json["choices"][0]["message"]["content"]
        return mensagem
    else:
        # Lidar com erros de chamada à API
        return None



def recomendacao_filmes(request):
    if request.method == 'POST':
        form = PerguntasForm(request.POST)
        if form.is_valid():
            respostas = form.cleaned_data

            
            recomendacao_filme = obter_recomendacao_filme(respostas)

            if recomendacao_filme:
                if '"' in recomendacao_filme:
                    nome_filme = recomendacao_filme.split('"')[1]
                else:
                    nome_filme = recomendacao_filme

            if recomendacao_filme:
                
                resposta_usuario = RespostasUsuario(
                    genero_filme_preferido=respostas['q1'],
                    sentimento_filmes_terror=respostas['q2'],
                    preferencia_filmes_contemporaneos=respostas['q3'],
                    protagonista_preferido=respostas['q4'],
                    final_emocionante_preferido=respostas['q5'],
                    sentimento_filmes_comedia_romantica=respostas['q6'],
                    diretor_favorito=respostas['q7'],
                    gosto_filmes_acao_adrenalina=respostas['q8'],
                    ator_atriz_favorito=respostas['q9'],
                    preferencia_filmes_fatos_reais_ficcao=respostas['q10'],
                    recomendacao_filme=nome_filme 
                )
                
                resposta_usuario.save()

                return render(request, 'respostas/index2.html', {'recomendacao_filme': recomendacao_filme})

    else:
        form = PerguntasForm()

    return render(request, 'src/index.html', {'form': form})



#TODO fazer o request do imdb, fazer a api ficar em modo unico 