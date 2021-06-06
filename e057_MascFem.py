# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
# ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor
# correto.

genero = str(input("Digite o sexo (M / F): ")).strip()[0]
while genero != "M" and genero != "F":
    print("Valor incorreto.")
    genero = str(input("Digite o sexo (M / F): ")).strip()
print(f"\nGênero {genero} registrado com sucesso.")


