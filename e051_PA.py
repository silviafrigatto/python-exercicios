# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite o valor da razão: "))
decimo = primeiro + (10 - 1) * razao
for valor in range(primeiro, decimo + razao, razao):
    print(valor, end=" ")
