# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input("- Continuar? [S/N]: ")).strip().upper()[0]
    while continuar not in "SsNn":
        continuar = str(input("- Opção inválida. Digite S ou N: "))
    if continuar in "Nn":
        break
print(f"Total de pessoas cadastradas: {len(pessoas)}")
print(f"Maior peso: {maior}kg")
for lista in pessoas:
    if lista[1] == maior:
        print(f"- {lista[0]}")
print(f"Menor peso: {menor}kg")
for lista in pessoas:
    if lista[1] == menor:
        print(f"- {lista[0]}")





