from django import forms

class PerguntasForm(forms.Form):
    q1 = forms.ChoiceField(choices=(('a', 'Ação'), ('b', 'Comédia'), ('c', 'Drama'), ('d', 'Ficção Científica'), ('e', 'Romance')), widget=forms.RadioSelect)

    q2 = forms.ChoiceField(choices=(('a', 'Adoro!'), ('b', 'Gosto de vez em quando.'), ('c', 'Não me importo.'), ('d', 'Não gosto muito.'), ('e', 'Odeio!')), widget=forms.RadioSelect)

    q3 = forms.ChoiceField(choices=(('a', 'Clássicos'), ('b', 'Contemporâneos'), ('c', 'Não tenho preferência.'), ('d', 'Depende do filme.'), ('e', 'Não assisto muitos filmes.')), widget=forms.RadioSelect)

    q4 = forms.ChoiceField(choices=(('a', 'Masculino'), ('b', 'Feminino'), ('c', 'Não tenho preferência.'), ('d', 'Dupla masculina/feminina'), ('e', 'Não tenho preferencia')), widget=forms.RadioSelect)

    q5 = forms.ChoiceField(choices=(('a', 'Final Feliz'), ('b', 'Final Surpreendente'), ('c', 'Final Aberto'), ('d', 'Final Triste'), ('e', 'Não tenho preferência.')), widget=forms.RadioSelect)

    q6 = forms.ChoiceField(choices=(('a', 'Amo!'), ('b', 'Gosto de vez em quando.'), ('c', 'Não me importo.'), ('d', 'Não gosto muito.'), ('e', 'Não suporto!')), widget=forms.RadioSelect)

    q7 = forms.ChoiceField(choices=(('a', 'Christopher Nolan'), ('b', 'Quentin Tarantino'), ('c', 'Martin Scorsese'), ('d', 'Greta Gerwig'), ('e', 'Não tenho preferencia')), widget=forms.RadioSelect)

    q8 = forms.ChoiceField(choices=(('a', 'Sim, adoro!'), ('b', 'Sim, gosto.'), ('c', 'Não me importo.'), ('d', 'Não muito.'), ('e', 'Não suporto.')), widget=forms.RadioSelect)

    q9 = forms.ChoiceField(choices=(('a', 'Tom Hanks'), ('b', 'Meryl Streep'), ('c', 'Leonardo DiCaprio'), ('d', 'Scarlett Johansson'), ('e', 'Não tenho preferencia')), widget=forms.RadioSelect)
    
    q10 = forms.ChoiceField(choices=(('a', 'Baseados em fatos reais'), ('b', 'Pura ficção'), ('c', 'Não tenho preferência.'), ('d', 'Depende do filme.'), ('e', 'Não assisto muitos filmes.')), widget=forms.RadioSelect)
