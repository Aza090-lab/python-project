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
#=====Usuários=====
usuarios_list = []
usuarios_list = list(storage.load('usuarios.json'))
what = "" #O tipo (nome ou e-mail) doq vai buscar
obj = "" # A coisa que vai buscar

#=====Projetos=====
projetos_list=[]
projetos_list=list(storage.load('projetos.json'))

#=====Tarefas=====
tarefas_list=[]
tarefas_list=list(storage.load('tarefas.json'))

#=====Usuários=====
#=====adiciona usuário=====
def add_user():
    usuario = {'NOME': utils.invalid_user_name(), 'E-MAIL': utils.invalid_user_email(usuarios_list), 'PERFIL': input("PERFIL...")}
    usuarios_list.append(usuario)
    storage.save(usuarios_list, 'usuarios.json')

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
            print("Usuário não encontrado!")
        else:
            obj = input("Digite o e-mail...")
            for i in range(len(usuarios_list)):
                if usuarios_list[i]['E-MAIL'].lower() == obj.lower():
                     print(usuarios_list[i])
                     return(i)
            print("Usuário não encontrado!")

#=====atualiza um usuário=====
def update_user():
     if len(usuarios_list)==0:
          print("Nenhum usuário cadastrado!")
          ui.main_ui()
     x = search_user()
     usuarios_list[x] = {'NOME': input("NOME..."), 'E-MAIL': input("E-MAIL..."), 'PERFIL': input("PERFIL...")} 
     storage.save(usuarios_list, 'usuarios.json')

#=====remove um usuário=====
def remove_user():
     if len(usuarios_list)==0:
          print("Nenhum usuário cadastrado!")
          ui.main_ui()
     x = search_user()
     del usuarios_list[x]
     storage.save(usuarios_list, 'usuarios.json')



#=====Projetos=====    
def cad_projetos():
    projeto={"id":input("digite o id do seu projeto:"),"nome":utils.invalid_user_project(projetos_list),"descricao":input("digite a descrição do seu projeto: "),"data_inicio":utils.tarefa_prazo(),"data_fim":""}
    projeto['data_fim'] = utils.invalid_date_end(projeto['data_inicio'])
    projetos_list.append(projeto)
    storage.save(projetos_list, 'projetos.json')

#=====Listar projetos=====
def listar_projetos():
    if len(projetos_list) == 0:
        print("Nenhum usuário cadastrado!")
    else:
        for i in projetos_list:
          print(i)
          '''
          print(f"id:{i['id']}")
          print(f"nome:{i['nome']}")
          print(f"descrição:{i['descricao']}")
          print(f"data_inicio:{i['data_inicio']}")
          print(f"data_fim:{i['data_fim']}")
          '''

#buscar
def buscar_projetos():
    if len(projetos_list) == 0:
        print("Nenhum usuário cadastrado!")
        ui.main_ui()

    id_projetos_list=input("Digite o id do projeto: ")
    encontrado=[]
    for projeto in projetos_list:
        if id_projetos_list in projeto ["id"]:
            encontrado.append(projeto)
    if not encontrado:
        print("Não encontrado!")
        return     
    print("Projeto Encontrado!")
    for i in encontrado:
        print(f"id:{i['id']}")
        print(f"nome:{i['nome']}")
        print(f"descrição:{i['descricao']}")
        print(f"data_inicio:{i['data_inicio']}")
        print(f"data_fim:{i['data_fim']}")

#atualizar
def atualizar_projetos():
    if len(projetos_list) == 0:
        print("Nenhum usuário cadastrado!")
        ui.main_ui()

    id_projetos_list=input("Digite o id do projeto: ")
    encontrado=[]
    for projeto in projetos_list:
        if id_projetos_list in projeto ["id"]:
            encontrado.append(projeto)
    if not encontrado:
        print("Não encontrado!")
        return     
    #print("Projeto Encontrado!")
    for i in encontrado:
        projeto={"id":input("digite o id do seu projeto:"),"nome":utils.invalid_user_project(projetos_list),"descricao":input("digite a descrição do seu projeto: "),"data_inicio":input("digite a data de início do seu projeto:"),"data_fim":input("digite a data do fim do seu projeto:")}
        '''
        i['id']=input("Digite o novo id do projeto:")
        i['nome']=input("Digite o novo nome do projeto:")
        i['descricao']=input("Digite a nova descrição do projeto:")
        i['data_inicio']=input("Digite a nova data de início do projeto:")
        i['data_fim']=input("Digite a nova data de fim do projeto:")
        '''
    storage.save(projetos_list, 'projetos.json')

#excluir
def excluir_projetos():
    if len(projetos_list) == 0:
        print("Nenhum usuário cadastrado!")
        ui.main_ui()

    id_projetos_list=input("Digite o id do projeto: ")
    for i,projeto in enumerate(projetos_list):
        if projeto["id"] == id_projetos_list:
            projetos_list.pop(i)
            print("Projeto Excluído!")
            storage.save(projetos_list, 'projetos.json')



#=====Tarefas=====
def add_tarefa():
    tarefa = {'TITULO': input("TITULO..."), 'PROJETOS': input("PROJETOS..."), 'RESPONSAVEL': input("RESPONSAVEL..."), 'STATUS':utils.tarefa_status(), 'PRAZO':utils.tarefa_prazo()}
    tarefas_list.append(tarefa)
    storage.save(tarefas_list, 'tarefas.json')

def list_tarefas():
    if len(tarefas_list) == 0:
        print("Nenhum usuário cadastrado!")

    else:
        choice = input('LISTAR por...\n[1] Todas\n[2] Projetos\n[3] Usuários\n[4] Status')
    
        if choice not in '1234':
         print("Opção invalida! Tente novamente...")
         ui.tarefas_ui()

        #Todas
        elif choice == '1':
          for i in range(len(tarefas_list)):
            print(tarefas_list[i])

        #Por projeto...
        elif choice == '2':
              x = buscar_tarefas("PROJETOS")

              if x != None:
                for i in tarefas_list:
                  if i["PROJETOS"] == tarefas_list[x]["PROJETOS"]:
                      print(tarefas_list[x])

        elif choice == '3':
            x = buscar_tarefas("RESPONSAVEL")

            if x != None:
                for i in tarefas_list:
                  if i["RESPONSAVEL"] == tarefas_list[x]["RESPONSAVEL"]:
                      print(tarefas_list[x])

        elif choice == '4':
             x = buscar_tarefas("STATUS")

             if x != None:
                for i in tarefas_list:
                  if i["STATUS"] == tarefas_list[x]["STATUS"]:
                      print(tarefas_list[x])

def buscar_tarefas(what):
    obj = input("Digte...")
    for i in range(len(tarefas_list)):
        if tarefas_list[i][what].lower() == obj.lower():
            return(i)
    print("Usuário não encontrado!")

def atualizar_tarefas():
    if len(tarefas_list)==0:
          print("Nenhuma tarefa cadastrada!")
          ui.main_ui()
    x = buscar_tarefas()
    tarefas_list[x] = {'TITULO': input("TITULO..."), 'PROJETOS': input("PROJETOS..."), 'RESPONSAVEL': input("RESPONSAVEL..."), 'STATUS':utils.tarefa_status(), 'PRAZO':utils.tarefa_prazo()}
    storage.save(tarefas_list, 'tarefas.json')

def remove_tarefas():
    if len(tarefas_list)==0:
          print("Nenhuma tarefa cadastrada!")
          ui.main_ui()
    x = buscar_tarefas()
    del tarefas_list[x]
    storage.save(tarefas_list, 'tarefas.json')