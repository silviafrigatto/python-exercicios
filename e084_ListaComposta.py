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
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input("Continuar? [S/N]: ")).strip().upper()[0]
    while continuar not in "SsNn":
        continuar = str(input("Opção inválida. Digite S ou N: "))
    if continuar in "Nn":
        break
#for p in pessoas:
 #   if p[1] == 0
print(pessoas)
print(f"Total de pessoas cadastradas: {len(pessoas)}")