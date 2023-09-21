
from django.shortcuts import render, redirect
from .forms import PerguntasForm
from .models import Filme

# Create your views here.
def home(request):
    return render(request,'src/index.html')

def index2(request):
    return render(request, 'respostas/index2.html')

def recomendacao_filmes(request):
    if request.method == 'POST':
        form = PerguntasForm(request.POST)
        if form.is_valid():
            # Obtenha as respostas do formulário
            respostas = form.cleaned_data

            # Mapeie as respostas de cada pergunta para index2
            opcoes_para_index2 = {
                'q1': 'a',
                'q2': 'b',
                'q3': 'c',
                'q4': 'd',
                'q5': 'e',
                'q6': 'a',
                'q7': 'b',
                'q8': 'c',
                'q9': 'd',
                'q10': 'e',
            }

            # Verifique se a resposta de cada pergunta corresponde à opção correspondente
            for pergunta, resposta_esperada in opcoes_para_index2.items():
                if respostas.get(pergunta) == resposta_esperada:
                    return redirect('index2')

            # Se nenhuma das respostas corresponder às respostas esperadas, renderize a página de perguntas novamente
            return render(request, 'src/index.html', {'form': form})
    else:
        form = PerguntasForm()

    return render(request, 'src/index.html', {'form': form})