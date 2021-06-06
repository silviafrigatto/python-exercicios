# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre elas (desconsiderando o flag).

cont = soma = 0
while True:
    num = int(input("Digite um número (ou 999 para encerrar o programa): "))
    if num == 999:
        break
    cont += 1
    soma += num
print("-" * 50)
print(f"Total de números digitados: {cont}\nTotal da soma: {soma}")


