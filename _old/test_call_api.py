import requests
import json

a = requests.get('https://dadosabertos.almg.gov.br/ws/proposicoes/pesquisa/direcionada?tp=1000&formato=json&ano=2023&ord=3')

a = a.json()

print("Chaves principais: ", a.keys())
resultado = a['resultado']
print("Chaves dentro de resultados: ", resultado.keys())
lista_item = resultado['listaItem']
print("\nTipo de dados dentro de 'listaItem':", type(lista_item))
print("\nTamanho da lista de itens: ", len(lista_item))
print("\nTamanho quantidade de valores de cada item: ", len(lista_item[0]))
print("\nTipo de informacoes de cada item: ", type(lista_item[0]))
lista_de_keys = ['dominio', 'tipoProjeto', 'siglaTipoProjeto', 'numero', 'ano', 'autor', 'ementa', 'indexacao',
                 'observacao', 'situacao', 'siglaSituacao', 'situacaoGeral', 'siglaSituacaoGeral', 'dataPublicacao',
                 'numeroDoc', 'proposicao', 'matricula', 'regime', 'local', 'norma', 'linkLegislacao',
                 'atualizacao', 'horario', 'atualizacaoTexto', 'horarioTexto', 'consultaPublica',
                 'dataUltimaAcao', 'tipoTramitacao', 'faseAtual', 'listaHistoricoTramitacoes', 'links',
                 'linksTextos', 'linksProposicoesAnexadas', 'proposicaoLei', 'consultaPublicaProposicao',
                 'acompanhamento', 'autoresEstruturados']
dict_item_de_cada = lista_item[0]
cont = 36
print(lista_de_keys[cont], ': ', dict_item_de_cada[lista_de_keys[cont]])
# print("\nPrimeiro item de 'listaItem':")
# print(json.dumps(lista_item[0]))
# print("\nChaves do primeiro item em 'listaItem':", lista_item[0].keys())
# print("\n'author' - Autor da proposição: ", lista_item[0]["autor"])
# print("\n'presentationDate' - Data de apresentação da proposição: ", f'{lista_item[0]["dataPublicacao"]}')

'''
Exemplo do primeiro item, e descricao se vai usar ou nao no banco.
0 - dominio :  Remissivo N
1 - tipoProjeto :  PROJETO DE LEI S ######################
2 - siglaTipoProjeto :  PL N
3 - numero :  1880 S ########################
4 - ano :  2023 S ##################
5 - autor :  Deputado Ricardo Campos S ####################
6 - ementa :  Declara de utilidade pública o Instituto de Desenvolvimento Social Dona Marly, com sede no Município de Montes Claros. S ##################
7 - indexacao :  /Tema/Municípios e Desenvolvimento Regional/Política Urbana/Região de Planejamento/Norte de Minas/Montes Claros (Microrregião)/Montes Claros /Tema/Administração Pública/Gestão Pública/Utilidade Pública N
8 - observacao :  Distribuído a 2 comissões: CJU TPA. N
9 - situacao :  Transformado em norma jurídica S ##################
10 - siglaSituacao :  TNJUR N
11 - situacaoGeral :  Proposições aprovadas N
12 - siglaSituacaoGeral :  MAPRV N
13 - dataPublicacao :  2024-02-09 N
14 - numeroDoc :  000005208 N
15 - proposicao :  PL. 1880 2023 - PROJETO DE LEI N
16 - matricula :  11307 N
17 - regime :  Deliberação em turno único nas comissões S ########################
18 - local :  Governador do Estado S ################
19 - norma :  LEI 24904 2024 - Lei Ordinária N
20 - linkLegislacao :  {'url': '/legislacao/mineira/LEI/24904/2024', 'rotulo': 'LEI 24904 2024 - Lei Ordinária'} N
21 - atualizacao :  20240718 N
22 - horario :  0755 N
23 - atualizacaoTexto :  20240708 N
24 - horarioTexto :  0722 N
25 - consultaPublica :  Consulta pública encerrada N
26 - dataUltimaAcao :  2024-07-17 N
27 - tipoTramitacao :  {'codigo': 3, 'nome': 'Regime de tramitação de deliberação em turno único nas comissões', 'listaFaseTramitacao': [{'codTipoTramitacao': 3, 'codigo': 1, 'nome': 'Apresentação', 'ordem': 1, 'descricao': '- O projeto foi recebido pela Mesa da Assembleia, numerado, publicado e encaminhado às Comissões para análise'}, {'codTipoTramitacao': 3, 'codigo': 2, 'nome': 'Turno único nas Comissões', 'ordem': 2, 'descricao': '- Comissões discutem o projeto e dão pareceres, que podem sugerir emendas ao texto original\r\n- Comissão discute e vota conclusivamente o projeto'}, {'codTipoTramitacao': 3, 'codigo': 3, 'nome': 'Redação final', 'ordem': 3, 'descricao': '- Comissão dá parecer sobre a redação final do projeto\r\n- Parecer é votado por Comissão'}, {'codTipoTramitacao': 3, 'codigo': 4, 'nome': 'Sanção, promulgação ou veto', 'ordem': 4, 'descricao': '- Governador recebe o projeto aprovado e pode transformá-lo em lei ou vetá-lo'}]} N
28 - faseAtual :  {'codTipoTramitacao': 3, 'codigo': 4, 'nome': 'Sanção, promulgação ou veto', 'ordem': 4, 'descricao': '- Governador recebe o projeto aprovado e pode transformá-lo em lei ou vetá-lo'} N
29 - "mata a tabela de Tramitação" - listaHistoricoTramitacoes S #############################
30 - links :  [] N
31 - linksTextos :  [{'expressao': '(PL.20230188001[codi])[txmt]', 'banco': 'mate', 'descricao': 'Proposição', 'url': '/proposicoes/pesquisa/avancada?expr=%28PL.20230188001%5Bcodi%5D%29%5Btxmt%5D&pesqProp=true'}, {'expressao': '(PL.202301880035[codi])[txmt]', 'banco': 'mate', 'descricao': 'Parecer de Turno Único - Comissão de Constituição e Justiça', 'url': '/proposicoes/pesquisa/avancada?expr=%28PL.202301880035%5Bcodi%5D%29%5Btxmt%5D&pesqProp=true'}, {'expressao': '(PL.202301880031076[codi])[txmt]', 'banco': 'mate', 'descricao': 'Parecer de Turno Único - Comissão do Trabalho, da Previdência e da Assistência Social', 'url': '/proposicoes/pesquisa/avancada?expr=%28PL.202301880031076%5Bcodi%5D%29%5Btxmt%5D&pesqProp=true'}, {'expressao': '(PL.2023018801013[codi])[txmt]', 'banco': 'mate', 'descricao': 'Parecer de Redação Final - Comissão de Redação', 'url': '/proposicoes/pesquisa/avancada?expr=%28PL.2023018801013%5Bcodi%5D%29%5Btxmt%5D&pesqProp=true'}, {'expressao': '(PL.20230188012[codi])[txmt]', 'banco': 'mate', 'descricao': 'Proposição de Lei', 'url': '/proposicoes/pesquisa/avancada?expr=%28PL.20230188012%5Bcodi%5D%29%5Btxmt%5D&pesqProp=true'}] N
32 - linksProposicoesAnexadas :  [] N
33 - proposicaoLei :  {'descricao': 'PRL 25866 2024'} N
34 - consultaPublicaProposicao :  {'idConsultaPublica': 72215, 'tipoProposicao': {'id': 1, 'descricao': 'Projeto de Lei', 'sigla': 'PL.', 'acompanhamento': 'S', 'pesquisaDirigida': 'S', 'idGrupoTipoProposicao': 5}, 'numeroProposicao': 1880, 'anoProposicao': 2023, 'dataInicio': {'@class': 'sql-timestamp', '$': '2024-02-07'}, 'moderada': 'N', 'votosFavoraveis': 0, 'votosContrarios': 0, 'qtdOpinioes': 0, 'totalRemovidoModerador': 0, 'totalRemovidoAutor': 0}
35 - acompanhamento :  N N
36 - autoresEstruturados :  [{'id': 11307, 'nome': 'Deputado Ricardo Campos', 'partido': 'PT'}] N
'''