# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços)
# – Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: ")).strip()
maiusculas = nome.upper()   # Transforma todas as letras em maiúsculas
minusculas = nome.lower()   # Transforma todas as letras em minúsculas
separar = nome.split()      # Cria uma lista com os nomes separados
juntar = "".join(separar)   # Junta os nomes em uma única string
letras_total = len(juntar)  # Conta o número de caracteres
nome01_total = len(separar[0])  # Conta o número de caracteres do primeiro nome
print(f"Seu nome em letras maiúsculas: {maiusculas}")
print(f"Seu nome em letras minúsculas: {minusculas}")
print(f"Número de letras do primeiro nome: {nome01_total}")
print(f"Número de letras do nome completo: {letras_total}")


