
# ==== RESUMO DE MÉTODOS DE STRING EM PYTHON ====

# .upper() — Tudo maiúsculo
nome = "ana"
print(nome.upper())  # ANA

# .lower() — Tudo minúsculo
frase = "Oi TUDO Bem?"
print(frase.lower())  # oi tudo bem?

# .strip() — Remove espaços no início e fim
texto = "   Olá mundo!   "
print(texto.strip())  # "Olá mundo!"

# .replace(antigo, novo) — Troca partes da string
mensagem = "Oi João"
print(mensagem.replace("João", "Maria"))  # Oi Maria

# .split() — Divide a string em partes (lista)
frase = "eu gosto de python"
print(frase.split())  # ['eu', 'gosto', 'de', 'python']

# .join(lista) — Junta elementos de uma lista em uma string
palavras = ['eu', 'gosto', 'de', 'python']
print(" ".join(palavras))  # eu gosto de python

# .find(texto) — Mostra a posição onde aparece
frase = "o rato roeu a roupa"
print(frase.find("roupa"))  # 15

# len() — Conta o número de caracteres
nome = "Luis"
print(len(nome))  # 4

# .capitalize() — Primeira letra maiúscula
texto = "python é legal"
print(texto.capitalize())  # Python é legal

# .count(texto) — Conta quantas vezes aparece
texto = "banana"
print(texto.count("a"))  # 3

# .isdigit() — Verifica se é número
x = "123"
print(x.isdigit())  # True

# .isalpha() — Verifica se são só letras
x = "abc"
print(x.isalpha())  # True

y = "abc123"
print(y.isalpha())  # False

# .isalnum() — Letras ou números (sem espaço!)
print("abc123".isalnum())  # True
print("abc 123".isalnum())  # False (por causa do espaço)

# Inverter string com fatiamento
texto = "python"
print(texto[::-1])  # nohtyp
