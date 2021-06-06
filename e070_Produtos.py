# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = cont_mil = menor_preco = 0
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço: R$"))
    continuar = str(input("Continuar? (S / N): ")).strip().upper()[0]
    print("-" * 30)
    barato = produto
    menor_preco = preco
    total += preco
    if preco >= 1000:
        cont_mil += 1
    if preco < menor_preco:
        menor_preco = preco
        barato = produto
    if continuar in "Nn":
        break
print(f"- Total da compra: R$ {total:.2f}")
print(f"- Produtos que custam acima de R$1000.00: {cont_mil}")
print(f"- Produto mais barato: {barato}")








