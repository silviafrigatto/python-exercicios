#  Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
#  que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print("\033[1;34m=-\033[m" * 39)
print("\033[1;44mDigite o comprimento de três segmentos e descubra se eles formam um triângulo.\033[m")
print("\033[1;34m=-\033[m" * 39)
l1 = float(input("\033[4mComprimento 1:\033[m "))
l2 = float(input("\033[4mComprimento 2:\033[m "))
l3 = float(input("\033[4mComprimento 3:\033[m "))

#if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
if ((l2 - l3) < l1 < (l2 + l3)) and ((l1 - l3) < l2 < (l1 + l3)) and ((l1 - l2) < l3 < (l1 + l2)):
    print("\033[34mÉ um triângulo:\033[m")
    if l1 == l2 == l3:
        print("* EQUILÁTERO - todos os lados iguais")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("* ISÓSCELES - dois lados iguais, um diferente")
    else:
        print("* ESCALENO - todos os lados diferentes")
else:
    print("\033[31mNão é triângulo.\033[m")
