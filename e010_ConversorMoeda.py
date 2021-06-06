# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
print("Bem vindo(a) ao conversor de moedas")
real = float(input("Digite o valor em reais: "))
usdolar = float(input("Digite a cotação do dólar na data de hoje: "))
print(f"Com R${real:.2f} você pode comprar US${real / usdolar:.2f} dólares.")
