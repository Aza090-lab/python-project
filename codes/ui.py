'''
=====Opções=====
Usuários (nome, e-mail, perfil)

Projetos (nome, descrição, data de início/fim)

Tarefas (título, status, responsável, prazo)

Usuários

=====Usuários=====
Cadastrar, listar, buscar por nome/e-mail, atualizar, remover.
Regras: e-mail único; nome não vazio.
'''
#=====Imports=====
import func

import os
import sys

#=====Limpar terminal=====
def clean():
    os.system('clear')

#=====Menu inicial de escolhas=====
def main_ui():
    print("="*10,"Gerenciador de Projetos","="*10)
    print("Opções:\n[1] Usuários\n[2] Projetos\n[3] Tarefas")
    
    chose = input("Digite uma opção...")

    if chose not in "123":
        print("Opção invalida! Tente novamente...")
        clean()
        main_ui()
    else:
        clean()
        #Usuários
        if chose == "1":
            usuarios_ui()
        #Projetos
        elif chose == "2":
            projetos_ui()
        #Tarefas
        else:
            tarefas_ui()

#=====Menu de escolhas Usuários=====
def usuarios_ui():
    print("="*10,"Usuários","="*10)
    print("[1] Cadastrar\n[2] listar\n[3] Buscar\n[4] Atualizar\n[5] Remover\n[0] Voltar")
    chose = input("Digite uma opção...")

    if chose not in "123450":
        print("Opção invalida! Tente novamente...")
        clean()
        usuarios_ui()
    
    else: 
        clean()
        #Voltar
        if chose == "0":
            main_ui()
        
        #Cadastrar
        elif chose == "1":
            func.add_user()
        
        #Listar
        elif chose == "2":
            func.list_users()
        
        #Buscar
        elif chose == "3":
            func.search_user()

        #Atualizar
        elif chose == "4":
            func.update_user()
        
        #Remover
        elif chose == "5":
            func.remove_user()
    main_ui()

#=====Menu de escolhas Projetos=====
def projetos_ui():
    print(func.cad_projetos)
    while True:
        print("="*10,"Cadastro de Projetos","="*10,"\n[1] Adicionar\n[2] Listar\n[3] Buscar\n[4] Atualizar\n[5] Excluir\n[6] Sair")
        opcao=input("Escolha uma opção!")
        if opcao == "1":
            func.cad_projetos_list()
        elif opcao == "2":
            func.listar_projetos_list()
        elif opcao == "3":
            func.buscar_projetos_list()
        elif opcao == "4":
            func.atualizar_projetos_list()
        elif opcao == "5":
            func.excluir_projetos_list()        
        elif opcao == "6"  :
            print("Saindo...")
     
            break 
        else:
            print("OPÇÃO INVÁLIDA!\n")
    main_ui()
#=====Menu de escolhas Tarefas=====
def tarefas_ui():
    print("="*10,"Usuários","="*10)
    print("[1] Cadastrar\n[2] listar \n[3] Atualizar\n[4] Remover\n[0] Voltar")
    chose = input("Digite uma opção...")
    
    if chose not in "123450":
        print ("opção invalida...tente novamente...")

    if chose=="1":
        func.add_tarefa()
    if chose=="2":
        func.list_tarefas()

    main_ui()
