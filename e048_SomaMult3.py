# Faça um programa que calcule a soma entre todos os números que são
# ímpares, múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
elementos = 0
for mult in range (3, 500, 6):
    soma += mult
    elementos += 1
    print(mult)
print(f"Existem {elementos} números entre 1 e 500 que são ímpares e múltiplos de 3.\nA soma de todos eles é igual a: {soma}.")



