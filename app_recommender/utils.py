import requests

API_KEY_TMDB = '32047b496cf842776a4b9f97135c846d'
BASE_URL_TMDB = 'https://api.themoviedb.org/3'

def obter_informacoes_filme_por_nome(nome_filme):
    url = f'{BASE_URL_TMDB}/search/movie'
    params = {'api_key': API_KEY_TMDB, 'query': nome_filme, 'language': 'pt-BR'}  # Defina o idioma como 'pt-BR'
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Verifique se há resultados de filmes
        if data.get('results'):
            # Pegue o primeiro resultado (o filme mais relevante)
            filme = data['results'][0]
            return filme
    return None

