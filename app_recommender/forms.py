from django import forms

class PerguntasForm(forms.Form):
    q1 = forms.ChoiceField(choices=(('a', 'Filmes'), ('b', 'Séries'), ('c', 'Documentários'), ('d', 'Novelas'), ('e', 'Outros')), widget=forms.RadioSelect)

    q2 = forms.ChoiceField(choices=(('a', 'Diretores renomados e premiados'), ('b', 'Diretores clássicos e atemporais'), ('c', 'Diretores contemporâneos em ascensão'), ('d', 'Diretores de mídia independente'), ('e', 'Não tenho preferência por tipo de diretor')), widget=forms.RadioSelect)

    q3 = forms.ChoiceField(choices=(('a', 'Curtametragem (geralmente menos de 30 minutos)'), ('b', 'Filmes longos (mais de 2 horas)'), ('c', 'Duração padrão (30 minutos a 2 horas)'), ('d', 'Depende do filme'), ('e', 'Não tenho preferência quanto à duração')), widget=forms.RadioSelect)

    q4 = forms.ChoiceField(choices=(('a', 'Enredo cativante'), ('b', 'Desenvolvimento de personagens'), ('c', 'Atuação excepcional'), ('d', 'Produção visual impressionante'), ('e', 'Mensagem ou tema poderoso')), widget=forms.RadioSelect)

    q5 = forms.ChoiceField(choices=(('a', 'Fatos Reais'), ('b', 'Ficção'), ('c', 'Uma mistura dos dois'), ('d', 'Depende do meu humor'), ('e', 'Não tenho preferência')), widget=forms.RadioSelect)

    q6 = forms.ChoiceField(choices=(('a', 'Noite'), ('b', 'Tarde'), ('c', 'Manhã'), ('d', 'Finais de semana'), ('e', 'Qualquer hora')), widget=forms.RadioSelect)

    q7 = forms.ChoiceField(choices=(('a', 'Sozinho'), ('b', 'Com a família'), ('c', 'Com amigos'), ('d', 'Com meu parceiro(a)'), ('e', 'Não tenho preferência, depende da mídia')), widget=forms.RadioSelect)

    q8 = forms.ChoiceField(choices=(('a', 'Nacional'), ('b', 'Internacional'), ('c', 'Com participação de brasileiros em produções internacionais'), ('d', 'Não tenho preferência, depende da mídia'), ('e', 'Gosto de todos igualmente')), widget=forms.RadioSelect)

    q9 = forms.ChoiceField(choices=(('a', 'Mídia reflexiva e profunda'), ('b', 'Mídia engraçada e leve'), ('c', 'Mídia tensa e emocionante'), ('d', 'Mídia intrigante e misteriosa'), ('e', 'Mídia repleta de ação')), widget=forms.RadioSelect)
    
    q10 = forms.ChoiceField(choices=(('a', 'Filmes mais recentes'), ('b', 'Filmes clássicos e antigos'), ('c', 'Gosto tanto de filmes recentes quanto de filmes clássicos'), ('d', 'Depende do meu humor'), ('e', 'Não tenho preferência')), widget=forms.RadioSelect)
