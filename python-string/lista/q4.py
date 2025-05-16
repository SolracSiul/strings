t = int(input("Questão 4 - Quantos casos de teste? "))
for _ in range(t):
    texto = input()
    resultado = ""
    for i in range(len(texto)):
        if i == 0 or texto[i] != texto[i - 1]:
            resultado += texto[i]
    print(resultado)