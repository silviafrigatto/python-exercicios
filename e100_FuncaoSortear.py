# Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
# e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
# entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep


def sorteia(lista):
    cont = 0
    while cont < 5:
        valor = randint(1, 10)
        if valor not in lista:
            lista.append(valor)
            cont += 1
    print("Números sorteados:\n=>", end=" ")
    for num in lista:
        sleep(.5)
        print(f"{num}", end=" ")


def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f"\nSoma dos números pares:\n=> {soma}")


numeros = []
sorteia(numeros)
sleep(1)
somaPar(numeros)

