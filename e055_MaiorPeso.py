# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual
# foi o maior e o menor peso lidos.

maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input(f"Digite o peso da {pessoa}ª pessoa (kg): "))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso lido foi: {maior}kg")
print(f"O menor peso lido foi: {menor}kg")


