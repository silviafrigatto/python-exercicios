# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input("Digite um ano e descubra se ele é bissexto: "))
if ano % 4 == 0 and ano % 100 != 0:
    print(f"{ano} é bissexto.")
elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print(f"{ano} é bissexto.")
else:
    print(f"{ano} não é bissexto.")
