notas = []

for i in range(4):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

print("\nNotas:", notas)

print("Maior nota:", max(notas))
print("Menor nota:", min(notas))

media = sum(notas) / len(notas)

print("Média:", media)

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")