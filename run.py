# === AULA DE MATRIZ EM PYTHON - PARTE PRÁTICA COM GABARITO ===

import random

# Exercício 1
print("\nExercício 1: Criar matriz 3x3 com números aleatórios de 1 a 50")
matriz1 = [[random.randint(1, 50) for j in range(3)] for i in range(3)]
for linha in matriz1:
    print(linha)

# Exercício 2
print("\nExercício 2: Preencher matriz 2x2 com números do usuário, exibir matriz e soma")

matriz2 = []
soma = 0
for i in range(2):
    linha = []
    for j in range(2):
        num = int(input(f"Digite o número para posição [{i}][{j}]: "))
        linha.append(num)
        soma += num
    matriz2.append(linha)

print("Matriz preenchida:")
for linha in matriz2:
    print(linha)

print(f"Soma dos elementos: {soma}")

# Exercício 3
print("\nExercício 3: Criar matriz 4x4 com zeros, alterar [2][3] para 99")

matriz3 = [[0 for j in range(4)] for i in range(4)]
matriz3[2][3] = 99

for linha in matriz3:
    print(linha)

# Exercício 4
print("\nExercício 4: Criar matriz 3x3 com soma dos índices (i + j)")

matriz4 = [[i + j for j in range(3)] for i in range(3)]

for linha in matriz4:
    for elemento in linha:
        print(elemento, end=" ")
    print()

# Exercício 5
print("\nExercício 5: Imprimir elementos maiores que 5 de uma matriz pré-definida")

matriz5 = [
    [1, 7, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Elementos maiores que 5:")
for linha in matriz5:
    for elemento in linha:
        if elemento > 5:
            print(elemento)

