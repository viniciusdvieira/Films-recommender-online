from django import forms

class PerguntasForm(forms.Form):
    q1 = forms.ChoiceField(choices=[('a', 'Ação'), ('b', 'Comédia'), ('c', 'Drama'), ('d', 'Ficção Científica'), ('e', 'Romance')], widget=forms.RadioSelect)
    # Adicione campos para outras perguntas aqui, se necessário