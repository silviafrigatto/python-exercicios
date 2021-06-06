# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

cateto_op = float(input("Digite a medida do cateto oposto: "))
cateto_ad = float(input("Digite a medida do cateto adjacente: "))
print(f"A hipotenusa mede {hypot(cateto_op, cateto_ad):.2f}.")

