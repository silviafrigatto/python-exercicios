# Crie um programa que leia um número Real qualquer pelo teclado e mostre
# na tela a sua porção Inteira.

# Opção 1
import math
num = float(input("Digite um número real: "))
print(f"A porção inteira do número {num} é {math.trunc(num)}.")

# Opção 2
# from math import trunc
# num = float(input("Digite um número real: "))
# print(f"A porção inteira do número {num} é {trunc(num)}.")

# Opção 3
# num = float(input("Digite um número real: "))
# print(f"A porção inteira do número {num} é {int(num)}.")