'''
Este arquivo deve ser utilizado apenas para coisas relacionadas ao salvamento e carregamento de arquivos json...
'''

import json

def save(dados, nome_arquivo = 'usuarios.json' ):
    with open(nome_arquivo, 'w', encoding = 'utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def load(nome_arquivo = 'usuarios.json'):
    try:
        with open(nome_arquivo, 'r', encoding= 'utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return{}
