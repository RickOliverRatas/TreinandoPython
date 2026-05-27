alunos = []


# Função para calcular média
def calcular_media(n1, n2):
    return (n1 + n2) / 2


# Função para cadastrar aluno
def cadastrar_aluno():
    nome = input("Nome do aluno: ")

    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))

    media = calcular_media(nota1, nota2)

    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "media": media
    }

    alunos.append(aluno)

    print("Aluno cadastrado com sucesso!")


# Função para listar alunos
def listar_alunos():

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    print("\nLISTA DE ALUNOS")

    for aluno in alunos:

        if aluno["media"] >= 7:
            status = "Aprovado"
        else:
            status = "Reprovado"

        print("----------------------")
        print("Nome:", aluno["nome"])
        print("Nota 1:", aluno["nota1"])
        print("Nota 2:", aluno["nota2"])
        print("Média:", aluno["media"])
        print("Status:", status)


# Menu principal
while True:

    print("\n===== SISTEMA =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")