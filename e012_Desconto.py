# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.
preco = float(input("Digite o preço do produto: R$"))
print(f"O preço com 5% de desconto é de R${preco - (preco * 5 / 100):.2f}.")
