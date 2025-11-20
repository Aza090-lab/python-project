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

#=====Menu inicial de escolhas=====
def main_ui():
    print("="*10,"Gerenciador de Projetos","="*10)
    print("Opções:\n[1] Usuários\n[2] Projetos\n[3] Tarefas")
    
    chose = input("Digite uma opção...")

    if chose not in "123":
        print("Opção invalida! Tente novamente...")
        main_ui()
    else:
        #Usuários
        if chose == "1":
            usuarios_ui()
        #Projetos
        elif chose == "2":
            print("2")
        #Tarefas
        else:
            print("3")

#=====Menu de escolhas Usuários=====
def usuarios_ui():
    print("="*10,"Usuários","="*10)
    print("[1] Cadastrar\n[2] listar\n[3] Buscar\n[4] Atualizar\n[5] Remover\n[0] Voltar")
    chose = input("Digite uma opção...")

    if chose not in "123450":
        print("Opção invalida! Tente novamente...")
        usuarios_ui()
    
    else: 
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