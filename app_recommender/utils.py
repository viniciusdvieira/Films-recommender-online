import requests

API_KEY_TMDB = '32047b496cf842776a4b9f97135c846d'
BASE_URL_TMDB = 'https://api.themoviedb.org/3'

def obter_id_trailer_youtube(filme_id):
    url = f'{BASE_URL_TMDB}/movie/{filme_id}/videos'
    params = {'api_key': API_KEY_TMDB, 'language': 'pt-BR'}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        trailers = [video for video in data.get('results', []) if video['type'] == 'Trailer']

        # Retorna o ID do primeiro trailer, se disponível
        if trailers:
            return trailers[0]['key']

    return None

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

                    elenco_principal = []

                    # Obtendo o elenco principal (os 5 primeiros atores)
                    for ator in credits_data.get('cast', [])[:10]:
                        ator_info = {
                            'name': ator['name'],
                            'profile_path': ator['profile_path'],
                            'character': None
                        }

                        # Fazendo uma chamada adicional para obter informações do personagem
                        personagem_response = requests.get(f'https://api.themoviedb.org/3/person/{ator["id"]}/movie_credits', params=params)
                        personagem_data = personagem_response.json()

                        # Verificando se há informações do personagem para o filme em questão
                        for movie_credit in personagem_data.get('cast', []):
                            if movie_credit.get('id') == filme_id:
                                ator_info['character'] = movie_credit.get('character')
                                break

                        elenco_principal.append(ator_info)



                    # Obtendo o nome do diretor
                    diretor = None
                    diretor_imagem = None
                    for membro_equipe in credits_data.get('crew', []):
                        if membro_equipe['job'] == 'Director':
                            diretor = membro_equipe['name']
                            diretor_imagem = membro_equipe.get('profile_path')  
                            break


                    # Obtendo informações sobre os vídeos associados ao filme
                    videos_url = f'{BASE_URL_TMDB}/movie/{filme_id}/videos'
                    params = {'api_key': API_KEY_TMDB, 'language': 'pt-BR'}
                    videos_response = requests.get(videos_url, params=params)
                    trailer_id = obter_id_trailer_youtube(filme_id)
                    if trailer_id:
                        filme['trailer_id'] = trailer_id  # Adicionando o ID do trailer

                    if videos_response.status_code == 200:
                        videos_data = videos_response.json()
                        trailers = [video for video in videos_data.get('results', []) if video['type'] == 'Trailer']

                        # Escolhendo o primeiro trailer, se disponível
                        if trailers:
                            trailer_id = trailers[0]['key']
                            filme['trailer_id'] = trailer_id  # Adicionando o ID do trailer




                    # Idioma Original
                    idioma_original = filme.get('original_language', 'Não disponível')

                    # Links para Redes Sociais
                    links_redes_sociais = filme.get('external_ids', {})
                    twitter = links_redes_sociais.get('twitter_id', 'Não disponível')
                    facebook = links_redes_sociais.get('facebook_id', 'Não disponível')
                    instagram = links_redes_sociais.get('instagram_id', 'Não disponível')

                    # Recomendações de Filmes Relacionados
                    recomendacoes_relacionadas = requests.get(f'{BASE_URL_TMDB}/movie/{filme_id}/recommendations', params=params)
                    if recomendacoes_relacionadas.status_code == 200:
                        recomendacoes_data = recomendacoes_relacionadas.json()
                        filmes_relacionados = recomendacoes_data.get('results', [])

                    filme['cast'] = elenco_principal
                    filme['runtime'] = duracao
                    filme['genres'] = generos
                    filme['diretor'] = diretor
                    filme['diretor_imagem'] = diretor_imagem
                    filme['idioma_original'] = idioma_original
                    filme['twitter'] = twitter
                    filme['facebook'] = facebook
                    filme['instagram'] = instagram
                    filme['filmes_relacionados'] = filmes_relacionados

                    return filme

    return None

