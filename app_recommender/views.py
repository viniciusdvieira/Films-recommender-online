
from django.shortcuts import render, redirect
from .forms import PerguntasForm
from config import API_KEY  # Importe a chave API
import requests
from .models import RespostaUsuario

# Create your views here.
def home(request):
    return render(request,'src/index.html')

def index2(request):
    return render(request, 'respostas/index2.html')

def obter_recomendacao_filme(respostas):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_modelo = "gpt-3.5-turbo"

    # Mapeamento das respostas completas com base nas opções disponíveis
    mapeamento_respostas = {
        'q1': {'a': 'Ação', 'b': 'Comédia', 'c': 'Drama', 'd': 'Ficção Científica', 'e': 'Romance'},
        'q2': {'a': 'Adoro!', 'b': 'Gosto de vez em quando.', 'c': 'Não me importo.', 'd': 'Não gosto muito.', 'e': 'Odeio!'},
        'q3': {'a': 'Clássicos', 'b': 'Contemporâneos', 'c': 'Não tenho preferência.', 'd': 'Depende do filme.', 'e': 'Não assisto muitos filmes.'},
        'q4': {'a': 'Masculino', 'b': 'Feminino', 'c': 'Não tenho preferência.', 'd': 'Dupla masculina/feminina', 'e': 'Outro (especifique)'},
        'q5': {'a': 'Final Feliz', 'b': 'Final Surpreendente', 'c': 'Final Aberto', 'd': 'Final Triste', 'e': 'Não tenho preferência.'},
        'q6': {'a': 'Amo!', 'b': 'Gosto de vez em quando.', 'c': 'Não me importo.', 'd': 'Não gosto muito.', 'e': 'Não suporto!'},
        'q7': {'a': 'Christopher Nolan', 'b': 'Quentin Tarantino', 'c': 'Martin Scorsese', 'd': 'Greta Gerwig', 'e': 'Outro (especifique)'},
        'q8': {'a': 'Sim, adoro!', 'b': 'Sim, gosto.', 'c': 'Não me importo.', 'd': 'Não muito.', 'e': 'Não suporto.'},
        'q9': {'a': 'Tom Hanks', 'b': 'Meryl Streep', 'c': 'Leonardo DiCaprio', 'd': 'Scarlett Johansson', 'e': 'Outro (especifique)'},
        'q10': {'a': 'Baseados em fatos reais', 'b': 'Pura ficção', 'c': 'Não tenho preferência.', 'd': 'Depende do filme.', 'e': 'Não assisto muitos filmes.'},
    }

    # Lista de perguntas
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
        {"role": "system", "content": "Você é um assistente de recomendação de filmes."}
    ]

    mensagens.extend(mensagem_final)
    #print(mensagens)
    
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

            # Chamar a função para obter a recomendação do filme
            recomendacao_filme = obter_recomendacao_filme(respostas)

            if recomendacao_filme:
                # Salvar as respostas do usuário no banco de dados
                usuario = request.user if request.user.is_authenticated else None
                for pergunta, resposta in respostas.items():
                    RespostaUsuario.objects.create(
                        usuario=usuario,
                        pergunta=pergunta,
                        resposta=resposta
                    )

                return render(request, 'respostas/index2.html', {'recomendacao_filme': recomendacao_filme})

    else:
        form = PerguntasForm()

    return render(request, 'src/index.html', {'form': form})


#TODO terminar o banco de resposta, e fazer o request do imdb, fazer a api ficar em modo unico 