usuarios = {"admin": "1234"}

while True:
    print("\n--- SISTEMA DE LOGIN ---")
    print("1. Cadastrar Usuário")
    print("2. Fazer Login")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_usuario = input("Digite o novo usuario: ")
        if novo_usuario in usuarios:
            print("Erro: Estre usuario ja existe!")
        else:
            nova_senha = input("Digite a senha: ")
            usuarios[novo_usuario] = nova_senha
            print("Usuario cadastrado com sucesso!")

    elif opcao == "2":

        usuario = input("Usuario: ")
        senha = input("Senha: ")

        if usuario in usuarios and usuarios[usuario] == senha:
            print(f"Bem vindo, {usuario}! Login realizado.")
            break
        else:
            print("Usuario ou senha incorretos.")
    
    elif opcao == "3":
        print("Saindo do sistema....")
        break
    else:
        print("Opção invalida!")