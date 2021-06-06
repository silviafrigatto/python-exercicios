# Faça um programa que leia um número inteiro e diga se ele é ou não um
# número primo.

num = int(input("Digite um número: "))
num_divisores = 0
print(f"{num} é divisível por: ", end="")
for divisor in range(num, 0, -1):
    if num % divisor == 0:
        num_divisores += 1
        print(divisor, end=" ")
if num_divisores == 2:
    print(f"\n{num} É PRIMO.")
else:
    print(f"\n{num} NÃO É PRIMO.")



