# Desenvolva um programa que leia o comprimento de três retas e diga
# ao usuário se elas podem ou não formar um triângulo.

print("\033[1;34m=-\033[m" * 39)
print("\033[1;44mDigite o comprimento de três segmentos e descubra se eles formam um triângulo.\033[m")
print("\033[1;34m=-\033[m" * 39)
c1 = float(input("\033[4mComprimento 1:\033[m "))
c2 = float(input("\033[4mComprimento 2:\033[m "))
c3 = float(input("\033[4mComprimento 3:\033[m "))

if ((c2 - c3) < c1 < (c2 + c3)) and ((c1 - c3) < c2 < (c1 + c3)) and ((c1 - c2) < c3 < (c1 + c2)):
    print("\033[34mÉ triângulo.\033[m")
else:
    print("\033[31mNão é triângulo.\033[m")