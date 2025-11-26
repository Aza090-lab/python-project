'''
Este arquivo deve ser utilizado apenas para coisas relacionadas ao salvamento e carregamento de arquivos json...
'''

#=====Imports=====
import json

#=====Salvamento de arquivos=====
def save(dados, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

#=====Carregamento de arquivos=====
def load(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
