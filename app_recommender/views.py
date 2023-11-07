from django.shortcuts import render
from .utils import obter_informacoes_midia_por_nome
from .forms import PerguntasForm
import requests
from .models import RespostasUsuario
from .models import FilmePesquisado
from cachetools import LRUCache
import hashlib
import os

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from dotenv import load_dotenv
load_dotenv(override=True)
keygpt = os.getenv("API_KEY")




recommendation_cache = LRUCache(maxsize=100)  # Cache com um tempo de vida de 1 hora (3600 segundos)



def home(request):
    return render(request,'src/index.html')

@csrf_exempt  # Você pode precisar desabilitar a proteção CSRF para essa view
def proxy_image(request, image_url):
    try:
        response = requests.get("https://image.tmdb.org/t/p/w500/" + image_url)
        
        # Certifique-se de que o status da resposta seja bem-sucedido antes de servir a imagem
        if response.status_code == 200:
            content_type = response.headers['Content-Type']
            return HttpResponse(response.content, content_type=content_type)
        else:
            return HttpResponse(status=500)  # Ou outro código de status apropriado
    except requests.exceptions.RequestException:
        return HttpResponse(status=500)  # Trate erros de solicitação

def obter_recomendacao_filme(respostas):
     # Crie uma chave única com base nas respostas do usuário para usar como chave de cache
    respostas_hash = hashlib.sha256(str(respostas).encode()).hexdigest()
    
    # Verifique se a recomendação já está em cache
    cached_recommendation = recommendation_cache.get(respostas_hash)
    if cached_recommendation:
        return cached_recommendation

    headers = {"Authorization": f"Bearer {keygpt}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_modelo = "gpt-3.5-turbo"

    
    mapeamento_respostas = {
        'q1': {'a': 'Filme', 'b': 'Série', 'c': 'Documentário', 'd': 'Animação(desenho animado)', 'e': 'Outros'},
        'q2': {'a': 'Diretores renomados e premiados', 'b': 'Diretores clássicos e atemporais', 'c': 'Diretores contemporâneos em ascensão', 'd': 'Diretores de mídia independente', 'e': 'Não tenho preferência por tipo de diretor'},
        'q3': {'a': 'Curtametragem', 'b': 'Midias longos ', 'c': 'Duração padrão ', 'd': 'Depende do filme', 'e': 'Não tenho preferência quanto à duração'},
        'q4': {'a': 'Enredo cativante', 'b': 'Desenvolvimento de personagens', 'c': 'Atuação excepcional', 'd': 'Produção visual impressionante', 'e': 'Mensagem ou tema poderoso'},
        'q5': {'a': 'Fatos Reais', 'b': 'Ficção', 'c': 'Uma mistura dos dois', 'd': 'Depende do meu humor', 'e': 'Não tenho preferência'},
        'q6': {'a': 'Noite', 'b': 'Tarde', 'c': 'Manhã', 'd': 'Finais de semana', 'e': 'Qualquer hora'},
        'q7': {'a': 'Sozinho', 'b': 'Com a família', 'c': 'Com amigos', 'd': 'Com meu parceiro(a)', 'e': 'Não tenho preferência, depende da mídia'},
        'q8': {'a': 'Nacional(Brasil)', 'b': 'Internacional', 'c': 'Com participação de brasileiros em produções internacionais', 'd': 'Não tenho preferência, depende da mídia', 'e': 'Gosto de todos igualmente'},
        'q9': {'a': 'Mídia reflexiva e profunda', 'b': 'Mídia engraçada e leve', 'c': 'Mídia tensa e emocionante', 'd': 'Mídia intrigante e misteriosa', 'e': 'Mídia repleta de ação'},
        'q10': {'a': 'Midias mais recentes', 'b': 'Midias clássicos e antigos', 'c': 'Gosto tanto de filmes recentes quanto de filmes clássicos', 'd': 'Depende do meu humor', 'e': 'Não tenho preferência'},
    }

    
    perguntas = [
        "Qual é o seu tipo preferido de mídia?",
        "Qual é o seu tipo preferido de diretor de mídia?",
        "Qual é a sua preferência em relação à duração da mídia?",
        "O que você valoriza mais em um conteúdo audiovisual?",
        "Você tende a preferir mídia baseada em fatos reais ou ficção completa?",
        "Qual é o momento ideal para você consumir mídia?",
        "Como você prefere consumir mídia?",
        "Você tem preferência por mídia nacional ou internacional?",
        "Que tipo de experiência midiática você está procurando agora?",
        "Você tende a preferir Midias mais recentes ou filmes clássicos e antigos?",
    ]

    # Depurar e verificar as perguntas e respostas
    print("Perguntas e respostas recebidas:")
    mensagens_formatadas = []
    for idx, (pergunta, resposta) in enumerate(zip(perguntas, respostas.values())):
        pergunta_formatada = f"{pergunta} {mapeamento_respostas[f'q{idx + 1}'][resposta]}"
        mensagens_formatadas.append(pergunta_formatada)
        print(f"Pergunta {idx + 1}: {pergunta_formatada}")

    mensagem_final = [
        {"role": "assistant", "content": "Recomende uma mídia audiovisual com base nas seguintes respostas:"},
        {"role": "system", "content": "Você é um assistente de recomendação de mídias audiovisuais. Concentre-se na primeira pergunta, pois ela é a mais importante logo as respsotas seguintes complementam a primeira. Evite recomendações repetidas.Não utilize informações de recomendações anteriores para recomendar uma nova"}
    ]


    # Montar as mensagens com perguntas e respostas formatadas
    mensagens = []
    for pergunta_formatada in mensagens_formatadas:
        mensagem_pergunta = {"role": "user", "content": pergunta_formatada}
        mensagens.extend([mensagem_pergunta])

    

    mensagens.extend(mensagem_final)
    print(mensagens)

    body_mensagem = {
        "model": id_modelo,
        "messages": mensagens
    }

    try:
        response = requests.post(link, headers=headers, json=body_mensagem)

        if response.status_code == 200:
            resposta_json = response.json()
            mensagem = resposta_json["choices"][0]["message"]["content"]
            recommendation_cache[respostas_hash] = mensagem  # Armazene a recomendação em cache
            return mensagem
        else:
            # Lidar com erros de chamada à API
            error_message = "Erro na chamada à API GPT-3.5 Turbo. Status code: {}".format(response.status_code)
            return error_message
    except requests.exceptions.RequestException as e:
        # Lidar com erros de conexão ou de rede
        return "Erro na conexão com a API: {}".format(str(e))



def recomendacao_filmes(request):
    if request.method == 'POST':
        form = PerguntasForm(request.POST)
        if form.is_valid():
            respostas = form.cleaned_data
            
            # Obter a recomendação de filme do chatbot (nome_filme é obtido da API do chatbot)
            recomendacao_filme = obter_recomendacao_filme(respostas)
            print(recomendacao_filme)
            if recomendacao_filme:
                if '"' in recomendacao_filme:
                    nome_filme = recomendacao_filme.split('"')[1]
                else:
                    nome_filme = recomendacao_filme

                # Obter informações detalhadas do filme usando a API TMDb
                filme = obter_informacoes_midia_por_nome(nome_filme)

                if filme:
                    # Salvar as respostas do usuário e a recomendação no banco de dados
                    resposta_usuario = RespostasUsuario(
                        pergunta1=respostas['q1'],
                        pergunta2=respostas['q2'],
                        pergunta3=respostas['q3'],
                        pergunta4=respostas['q4'],
                        pergunta5=respostas['q5'],
                        pergunta6=respostas['q6'],
                        pergunta7=respostas['q7'],
                        pergunta8=respostas['q8'],
                        pergunta9=respostas['q9'],
                        pergunta10=respostas['q10'],
                        recomendacao_filme=nome_filme
                    )
                    resposta_usuario.save()

                    # Renderizar a página 'index2.html' com informações do filme
                    return render(request, 'respostas/index2.html', {'recomendacao_filme': recomendacao_filme, 'filme': filme})

    else:
        form = PerguntasForm()
        nome_filme = request.GET.get('q')  # Obter o nome do filme da consulta GET

        if nome_filme:
            # Salvar o nome do filme pesquisado no banco de dados
            pesquisa = FilmePesquisado(nome_filme=nome_filme)
            pesquisa.save()

            # Obter informações do filme com base no nome
            filme = obter_informacoes_midia_por_nome(nome_filme)
            
            if filme:
                # Renderizar a página 'index2.html' com informações do filme
                return render(request, 'respostas/index2.html', {'filme': filme, 'form': form})

    # Recuperar todas as pesquisas anteriores
    pesquisas_anteriores = FilmePesquisado.objects.all().order_by('-data_pesquisa')
    
    return render(request, 'src/index.html', {'form': form, 'pesquisas_anteriores': pesquisas_anteriores})





#TODO Fazer o dos jogos e livros, continuar a estilização
#api de jogos https://rawg.io/apidocs
#api de livros https://developers.google.com/books?hl=pt-br


#alterações futuras: https://chat.openai.com/share/37b6da64-4145-4ce9-b114-1070cd8c5879 Este chat representa como seria a implementação da ia para ela gerar tambem as perguntas, como o tempo é pouco vai ficar para depois do projeto pronto