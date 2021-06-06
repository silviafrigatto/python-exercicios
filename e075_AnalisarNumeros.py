# Desenvolva um programa que leia quatro valores pelo teclado e
# guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


num = (int(input("Digite o 1º número: ")), int(input("Digite o 2º número: ")),
       int(input("Digite o 3º número: ")), int(input("Digite o 4º número: ")))
cont_impares = 0
#  Analisar o número 9
if num.count(9) == 1:
    print(f"O número 9 apareceu {num.count(9)} vez.")
else:
    print(f"O número 9 apareceu {num.count(9)} vezes.")
#  Analisar o número 3:
if 3 in num:
    print(f"O número 3 foi digitado na {num.index(3) + 1}ª posição.")
else:
    print("O número 3 não foi digitado.")
#  Analisar números pares
pares = []
for valor in num:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        cont_impares += 1
if cont_impares == 4:
    print("Não foram digitados números pares.")
else:
    print("Você digitou os seguintes números pares: ", end="")
    for elemento in pares:
        print(elemento, end=" ")




