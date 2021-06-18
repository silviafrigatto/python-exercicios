# Faça um programa que tenha uma função chamada maior(), que receba vários
# parâmetros com valores inteiros. Seu programa tem que analisar todos os
# valores e dizer qual deles é o maior.


from time import sleep


def maior(*num):
    print("*-" * 30)
    print(f"Os valores informados foram:", end=" ")
    for valor in num:
        sleep(.5)
        print(f"{valor}", end=" ")
    sleep(.5)
    if len(num) == 0:
        num = 0
        print(f"\nTotal de números informados: {num}")
        print(f"O maior valor informado foi: {num}")
    else:
        print(f"\nTotal de números informados: {len(num)}")
        print(f"O maior valor informado foi: {max(num)}")
    sleep(2)


maior(1, 2, 3)
maior(1, 5, 7, 4)
maior(5, 1, 25, 10, 2)
maior(-10, -20)
maior()




