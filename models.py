import json
usuario = {}

def in_usuario():
    global usuario = {"id" : input("Digite o id: "), "name" : input("Digite o nome: "), "perfil" : input("Digite o perfil: ") }
    
    global usuario = "usuario.json"
