# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import sqrt

cateto_op = float(input("Digite o comprimento do cateto oposto: "))
cateto_ad = float(input("Digite o comprimento do cateto adjacente: "))
quadrado_op = pow(cateto_op, 2)
quadrado_ad = pow(cateto_ad, 2)
print(f"Hipotenusa = {sqrt(quadrado_ad + quadrado_op):.2f}.")

