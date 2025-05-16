
nome = input("Questão 3 - Digite o nome: ")
i = 1
while i <= len(nome):
    #se fossemos escrever isso em uma forma seria: escreva até essa posicao: [:2] até o index 2...
    print(nome[:i].upper())
    i += 1
