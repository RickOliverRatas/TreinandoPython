compras = []

while True:
    print("1. Adicionar")
    print("2. Remover")
    print("3. Listar")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
            compras.append(input("Digite o nome do item: "))
            print("item adicionado com sucesso!")

    elif opcao == "2":
              
        print(compras)
        item = input("Quais item deseja remover? ")
        
        if item in compras:
                compras.remove(item)  
        else:
                print("item nao encontrado")

    elif opcao == "3":
            print("Lista de compras: ")
            for item in compras:
                print(item)

    elif opcao == "4":
            print("Saindo do sistema")
            break
    else:
            print("opção invalida!")
        
