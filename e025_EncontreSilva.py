# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input("Digite o nome completo: ")).strip().upper()
print(f"Esse nome tem SILVA?", "SILVA" in nome)
