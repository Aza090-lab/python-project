'''
Este arquivo deve ser usado para as validações com o uso de 'try' e 'except'...
favor, evitar fazer funções repetidas e tentar fazer funções compactas...
'''
#=====imports=====
import func

#=====nome de usuário invalido=====
def invalid_user_name():
    name = input("NOME...")
    while(name== ""):
        print("NOME inválido! Tente novamente... ")
        name = input("NOME...")
    return(name)

#=====endereço de e-mail invalido=====
def invalid_user_email(usuario_list):
    email = input("E-MAIL...")
    while no_repet(email, usuario_list) == False:
        print("E-MAIL já foi registrado! Tente outro...")
        email = input("E-MAIL...")
    return(email)

#=====verifica se o e-mail ja foi cadastrado=====
def no_repet(email, usuario_list):
    for i in usuario_list:
        if i['E-MAIL'] == email:
            return(False)
    return(True)