import requests
import json

a = requests.get('https://dadosabertos.almg.gov.br/ws/proposicoes/pesquisa/direcionada?tp=1000&formato=json&ano=2023&ord=3')

a = a.json()

print("Chaves principais: ", a.keys())
resultado = a['resultado']
print("Chaves dentro de resultados: ", resultado.keys())
lista_item = resultado['listaItem']
print("\nTipo de dados dentro de 'listaItem':", type(lista_item))
print("\nPrimeiro item de 'listaItem':")
print(json.dumps(lista_item[0], indent=4, ensure_ascii=False))
print("\nChaves do primeiro item em 'listaItem':", lista_item[0].keys())