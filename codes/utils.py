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

#=====Validação status da tarefa=====
def tarefa_status ():
    print ("STATUS...\npendente [1]\n andamento [2]\n concluida [3]")
    choice = input("Digite uma opção...")
    if choice not in "123":
        print ("opção invalida")
    elif choice==1:
        return('Pendente')
    elif choice==2:
        return('andamento')
    elif choice==3:
        return('concluido')
    
#=====Validação prazo da tarefa=====
def tarefa_prazo():
    print("DATA(YYYY-MM-DD)...")

    ano= int(input("ANO..."))

    while ano < 0:
        print ("Ano invalido! Digite novamente...")
        ano= int (input("ANO..."))

    mes= int (input("MÊS..."))

    while mes > 12 or mes<= 0:
        print ("Mês invalido! Digite novamente...")
        mes= int (input("MÊS..."))

    dia= int(input("DIA..."))

    while dia > 31 or dia<= 0:
        print ("Dia invalido! Digite novamente...")
        dia= int (input("DIA..."))

    print (ano,"-", mes,"-",dia )


            

