frase = input("Questão 2 - Digite a frase: ")
nova_frase = ""
for letra in frase:
    if not letra.isdigit():
        nova_frase += letra
print(nova_frase)