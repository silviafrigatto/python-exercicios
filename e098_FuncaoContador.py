# Faça um programa que tenha uma função chamada contador(), que receba
# três parâmetros: início, fim e passo. Seu programa tem que realizar
# três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    sleep(2.5)
    if passo == 0:
        passo = 1
    if inicio < fim:
        if passo < 0:
            passo = -(passo)
        for num in range(inicio, fim + 1, passo):
            sleep(.5)
            print(f"{num}", end=" ")
        print("FIM!")
    else:
        if passo > 0:
            passo = -(passo)
        for num in range(inicio, fim - 1, passo):
            sleep(.5)
            print(f"{num}", end=" ")
        print("FIM!")


def escreva(string):
    tamanho = len(string)
    print("-" * tamanho)
    print(string)
    print("-" * len(string))


escreva("Contagem de 1 a 10, de 1 em 1:")
contador(1, 10, 1)
sleep(1)
escreva("Contagem de 10 a 0, de 2 em 2:")
contador(10, 0, -2)
sleep(1)
print("\nAgora é a sua vez de personalizar a contagem: ")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
escreva(f"Contagem de {i} a {f}, de {p} em {p}:")
contador(i, f, p)


