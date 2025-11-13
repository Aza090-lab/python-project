import json
import ui

usuario = {}
usuarios_list = []

def in_usuario():
    global usuario
    global usuarios_list
    usuario = {"id" : input("Digite o id: "), "name" : input("Digite o nome: "), "perfil" : input("Digite o perfil: ") }
    usuarios_list.append(usuario)
    #usuarios_list = "usuario.json"
    ui.main_ui()

def return_usuario():
    global usuarios_list
    for i in range(len(usuarios_list)):
        print(usuarios_list[i])
    ui.main_ui()