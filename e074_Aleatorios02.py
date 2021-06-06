# Crie um programa que vai gerar cinco números aleatórios e colocar
# em uma tupla. Depois disso, mostre a listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla.

from random import randint

aleatorios = (randint(0, 100), randint(0, 100), randint(0, 100),
              randint(0, 100), randint(0, 100))
for numero in aleatorios:
    print(f"{numero}", end=" ")
print(f"\nMaior: {max(aleatorios)}")
print(f"Menor: {min(aleatorios)}")