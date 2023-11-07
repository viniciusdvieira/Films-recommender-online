import requests

API_KEY_TMDB = '32047b496cf842776a4b9f97135c846d'
BASE_URL_TMDB = 'https://api.themoviedb.org/3'

def obter_informacoes_midia_por_nome(nome_midia):
    url = f'{BASE_URL_TMDB}/search/multi'  # Pesquisa tanto filmes quanto séries
    params = {'api_key': API_KEY_TMDB, 'query': nome_midia, 'language': 'pt-BR'}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data.get('results'):
            # Procurar o melhor resultado que corresponde ao nome fornecido
            for midia in data['results']:
                if midia.get('id'):
                    midia_id = midia['id']
                    details_url = f'{BASE_URL_TMDB}/movie/{midia_id}'
                    credits_url = f'{BASE_URL_TMDB}/movie/{midia_id}/credits'
                    params = {'api_key': API_KEY_TMDB, 'language': 'pt-BR'}
                    details_response = requests.get(details_url, params=params)
                    credits_response = requests.get(credits_url, params=params)

                    if details_response.status_code == 200 and credits_response.status_code == 200:
                        details_data = details_response.json()
                        credits_data = credits_response.json()

                        # Obtendo a duração da mídia (filme ou série)
                        duracao = details_data.get('runtime', 0)

                        # Obtendo os gêneros da mídia
                        generos = details_data.get('genres', [])

                        # Obtendo o elenco principal (os 5 primeiros atores)
                        elenco_principal = []
                        for ator in credits_data.get('cast', [])[:5]:
                            ator_info = {
                                'name': ator['name'],
                                'profile_path': ator['profile_path']
                            }
                            elenco_principal.append(ator_info)

                        # Obtendo o nome do diretor
                        diretor = None
                        diretor_imagem = None
                        for membro_equipe in credits_data.get('crew', []):
                            if membro_equipe['job'] == 'Director':
                                diretor = membro_equipe['name']
                                diretor_imagem = membro_equipe.get('profile_path')
                                break

                        midia['cast'] = elenco_principal
                        midia['runtime'] = duracao
                        midia['genres'] = generos
                        midia['diretor'] = diretor
                        midia['diretor_imagem'] = diretor_imagem

                        return midia

    return None
