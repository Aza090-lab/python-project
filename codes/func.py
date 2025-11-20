'''
Esse arqui deve servir APENAS para funções, como busca e coisas relacionadas...
favor, evitar modificar arquidos já prontos, e caso edite, coloque com um '#' qual a mudança feita e por quem...
incluse evitem criar funções repetidas...
'''

#=====imports=====
import ui
#=====Variaveis=====
usuarios_list = []

def add_user():
    usuario = {'NOME': input("NOME..."), 'E-MAIL': input("E-MAIL..."), 'PERFIL': input("PERFIL...")}
    usuarios_list.append(usuario)

def list_users():
    if len(usuarios_list) == 0:
        print("Nenhum usuário cadastrado!")

    for i in range(len(usuarios_list)):
        print(usuarios_list[i])

def search_user():
    if len(usuarios_list) == 0:
                print("Nenhum usuário cadastrado!")
                main_ui()

    print("Buscar por...\n[1] Nome\n[2] E-mail")
    what = input("...")

    if what not in "12":
        print("Opção invalida! Tente novamente...")
        ui.main_ui()
    else:
        if what == "1":
            obj = input("Digte o nome...")
            for i in usuarios_list:
                if i['NOME'] == obj:
                     print(i)
                     break
                else:
                     print("Usuário não encontrado!")
        else:
            obj = input("Digite o e-mail...")
            for i in usuarios_list:
                if i['NOME'] == obj:
                    print(i)
                    break
                else:
                    print("Usuário não encontrado!")
        
