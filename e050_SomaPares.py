# Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
num_pares = 0
for num in range(1, 7):
    n1 = int(input("Digite um número: "))
    if n1 % 2 == 0:
        soma += n1
        num_pares += 1
print(f"Você digitou {num_pares} números PARES.\nA soma deles é igual a {soma}.")