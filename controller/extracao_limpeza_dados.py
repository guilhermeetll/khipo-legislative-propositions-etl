import requests
import json
from datetime import datetime

# Faz a solicitação à API
url = "https://dadosabertos.almg.gov.br/ws/proposicoes/pesquisa/direcionada?tp=1000&formato=json&ano=2023&ord=3"
response = requests.get(url)
data = response.json()

# Verifica a existência de 'listaItem' e inspeciona seu conteúdo
if 'listaItem' in data['resultado']:
    lista_item = data['resultado']['listaItem']
    
    proposicoes = []
    tramitacoes = []

    for item in lista_item:
        proposicao = {
            'author': item.get('autor', '').strip(),
            'presentationDate': datetime.strptime(item.get('dataPublicacao', ''), '%Y-%m-%d') if item.get('dataPublicacao') else None,
            'ementa': item.get('assunto', '').replace('\n', ' ').strip(),
            'regime': item.get('regime', '').strip(),
            'situation': item.get('situacao', '').strip(),
            'propositionType': item.get('tipoProjeto', '').strip(),
            'number': item.get('numero', '').strip(),
            'year': int(item.get('ano', 0)),
            'city': 'Belo Horizonte',
            'state': 'Minas Gerais'
        }
        proposicoes.append(proposicao)

        if 'listaHistoricoTramitacoes' in item:
            for hist in item['listaHistoricoTramitacoes']:
                tramitacao = {
                    'createAt': datetime.strptime(hist.get('data', ''), '%Y-%m-%d') if hist.get('data') else None,
                    'description': hist.get('historico', '').replace('\n', ' ').strip(),
                    'local': hist.get('local', '').strip(),
                    'propositionId': item.get('numeroDoc', '').strip()  # Ajuste conforme necessário para referenciar o ID da proposição
                }
                tramitacoes.append(tramitacao)

    print("Proposicoes:", json.dumps(proposicoes, indent=4, ensure_ascii=False))
    print("Tramitacoes:", json.dumps(tramitacoes, indent=4, ensure_ascii=False))
else:
    print("A chave 'listaItem' não foi encontrada em 'resultado'.")