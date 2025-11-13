import models

def main_ui():
    print("====== Gerenciador De Projetos ======\n[1] Usuários\n[2] Projetos\n[3] Tarefas")
    m = input("...")
    if m not in "123":
        print("Ação invalida! Tente novamente...")
        main_ui()
    elif m == "1":
        usuario_ui()
    elif m == "2":
        print("\nProjetos...")
    else:
        print("\nTarefas...")

def usuario_ui():
    print("====== Usuários =====\n[1] Cadastrar\n[2] listar\n[3] Buscar\n[4] Atualizar\n[5] Remover ")
    m = input("...")
    if m not in "12345":
        print("Ação invalida! Tente novamente...")
        usuario_ui()
    elif m == "1":
        models.in_usuario()
    elif m == "2":
        print(models.return_usuario())