# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é
# a condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag).

num = int(input("Digite um número ou 999 para encerrar o programa: "))
soma = cont_num = 0
while num != 999:
    soma += num
    cont_num += 1
    num = int(input("Digite um número ou 999 para encerrar o programa: "))
print(f"Total de números digitados: {cont_num}")
print(f"Soma dos números digitados: {soma}")



