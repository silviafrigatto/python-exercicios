# Crie um programa que vai gerar cinco números aleatórios e colocar
# em uma tupla. Depois disso, mostre a listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla.

from random import randint

aleatorios = ()
lista_aleatorios = list(aleatorios)
for etapa in range (0, 5):
    num_comp = randint(0, 100)
    lista_aleatorios.append(num_comp)
aleatorios = tuple(sorted(lista_aleatorios))
print("*" * 47)
print("\033[1mGERADOR DE NÚMEROS\033[m")
print("*" * 47)
print(f"Números em ordem aleatória: {lista_aleatorios}")
print(f"Números em ordem crescente: {aleatorios}")
print(f"Menor: {aleatorios[0]}\nMaior: {aleatorios[-1]}")
