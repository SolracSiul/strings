print("Questão 5 - Digite frases. Digite 'FIM' para encerrar.")
while True:
    frase = input()
    if frase.strip().upper() == "FIM":
        break
    print(frase[::-1])