# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

import math

ang = float(input("Digite o ângulo: "))
rad = math.radians(ang)  # Converte o ângulo digitado em radianos.
print(f"O SENO de {ang}º é {math.sin(rad):.2f}.")
print(f"O COSSENO de {ang}º é {math.cos(rad):.2f}.")
print(f"A TANGENTE de {ang}º é {math.tan(rad):.2f}.")
