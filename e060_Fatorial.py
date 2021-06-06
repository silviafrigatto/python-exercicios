#  Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

num = int(input("Digite um número para calcular seu fatorial: "))
cont = num
while cont != 0:
    if cont == 1:
        print(cont, end=" = ")
    else:
        print(cont, end=" x ")
    cont -= 1
print(factorial(num))


