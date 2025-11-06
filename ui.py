def main_ui():
    print("=== Gerenciador De Projetos ===\n[1] Usuários\n[2] Projetos\n[3] Tarefas")
    m = input("...")
    if m not in "123":
        print("Ação invalida! Tente novamente...")
        main_ui()
    elif m == "1":
        print("\nUsuários...")
    elif m == "2":
        print("\nProjetos...")
    else:
        print("\nTarefas...")


main_ui()
