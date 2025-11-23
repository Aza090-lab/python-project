'''
Esse arqui deve servir APENAS para funções, como busca e coisas relacionadas...
favor, evitar modificar arquidos já prontos, e caso edite, coloque com um '#' qual a mudança feita e por quem...
incluse evitem criar funções repetidas...
'''

#=====imports=====
import ui
import utils
import storage

#=====Variaveis=====
usuarios_list = []
what = "" #O tipo (nome ou e-mail) doq vai buscar
obj = "" # A coisa que vai buscar

#=====adiciona usuário=====
def add_user():
    usuario = {'NOME': utils.invalid_user_name(), 'E-MAIL': utils.invalid_user_email(usuarios_list), 'PERFIL': input("PERFIL...")}
    usuarios_list.append(usuario)

#=====lista os usuários=====
def list_users():
    if len(usuarios_list) == 0:
        print("Nenhum usuário cadastrado!")

    for i in range(len(usuarios_list)):
        print(usuarios_list[i])

#=====busca por um usuário=====
def search_user():
    if len(usuarios_list) == 0:
                print("Nenhum usuário cadastrado!")
                ui.main_ui()

    print("Buscar por...\n[1] Nome\n[2] E-mail")
    what = input("...")

    if what not in "12":
        print("Opção invalida! Tente novamente...")
        ui.main_ui()
    else:
        if what == "1":
            obj = input("Digte o nome...")
            for i in range(len(usuarios_list)):
                if usuarios_list[i]['NOME'].lower() == obj.lower():
                     print(usuarios_list[i])
                     return(i)
                else:
                     print("Usuário não encontrado!")
        else:
            obj = input("Digite o e-mail...")
            for i in range(len(usuarios_list)):
                if usuarios_list[i]['E-MAIL'].lower() == obj.lower():
                     print(usuarios_list[i])
                     return(i)
                else:
                    print("Usuário não encontrado!")

#=====atualiza um usuário=====
def update_user():
     if len(usuarios_list)==0:
          print("Nenhum usuário cadastrado!")
          ui.main_ui()
     x = search_user()
     usuarios_list[x] = {'NOME': input("NOME..."), 'E-MAIL': input("E-MAIL..."), 'PERFIL': input("PERFIL...")} 

#=====remove um usuário=====
def remove_user():
     if len(usuarios_list)==0:
          print("Nenhum usuário cadastrado!")
          ui.main_ui()
     x = search_user()
     del usuarios_list[x]

     