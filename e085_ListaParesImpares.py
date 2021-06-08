# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores
# pares e ímpares. No final, mostre os valores pares e ímpares em ordem
# crescente.

numeros = [[], []]
valor = 0
for num in range(1, 8):
    valor = int(input(f"Digite o {num}º valor: "))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print(f"Valores pares: {sorted(numeros[0])}")
print(f"Valores ímpares: {sorted(numeros[1])}")

