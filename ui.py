def main_ui():
    print("\n=== Gerenciador De Projetos ===\n[1] Usuários\n[2] Projetos\n[3] Tarefas")
    m = input("\n...")
    if m not in "1234567890":
        print("\nAÇÃO INVALIDA!!!!")
        main_ui()
    else:
        print("a")
main_ui()
