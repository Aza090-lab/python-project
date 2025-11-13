import models

def main_ui():
    print("====== Gerenciador De Projetos ======\n[1] Usuários\n[2] Projetos\n[3] Tarefas")
    m = input("...")
    if m not in "123":
        print("Ação invalida! Tente novamente...")
        main_ui()
    elif m == "1":
        #print("\nUsuários...")
        usuario_ui()
        #in_usuario = models.in_usuario()
    elif m == "2":
        print("\nProjetos...")
    else:
        print("\nTarefas...")

def usuario_ui():
    print("====== Usuários =====\n[1] Cadastrar\n[2] listar\n[3] Buscar\n[4] Atualizar\n[5] Remover ")
