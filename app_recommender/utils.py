import requests

API_KEY_TMDB = '32047b496cf842776a4b9f97135c846d'
BASE_URL_TMDB = 'https://api.themoviedb.org/3'

def obter_informacoes_filme_por_nome(nome_filme):
    url = f'{BASE_URL_TMDB}/search/movie'
    params = {'api_key': API_KEY_TMDB, 'query': nome_filme, 'language': 'pt-BR'}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data.get('results'):
            filme = data['results'][0]
            if filme.get('id'):
                filme_id = filme['id']
                details_url = f'{BASE_URL_TMDB}/movie/{filme_id}'
                credits_url = f'{BASE_URL_TMDB}/movie/{filme_id}/credits'
                params = {'api_key': API_KEY_TMDB, 'language': 'pt-BR'}
                details_response = requests.get(details_url, params=params)
                credits_response = requests.get(credits_url, params=params)

                if details_response.status_code == 200 and credits_response.status_code == 200:
                    details_data = details_response.json()
                    credits_data = credits_response.json()

                    # Obtendo a duração do filme
                    duracao = details_data.get('runtime', 0)

                    # Obtendo os gêneros do filme
                    generos = details_data.get('genres', [])

                    # Obtendo o elenco principal (os 5 primeiros atores)
                    elenco_principal = []
                    for ator in credits_data.get('cast', [])[:5]:
                        ator_info = {
                            'name': ator['name'],
                            'profile_path': ator['profile_path']
                        }
                        elenco_principal.append(ator_info)

                    filme['cast'] = elenco_principal
                    filme['runtime'] = duracao  # Add movie duration
                    filme['genres'] = generos  # Add movie genres

                    return filme

    return None
