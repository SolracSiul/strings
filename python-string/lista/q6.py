n = int(input("Questão 6 - Quantas frases para verificar palíndromo? "))
for _ in range(n):
    frase = input()
    limpa = frase.lower().replace(" ", "")
    if limpa == limpa[::-1]:
        print("SIM")
    else:
        print("NAO")
