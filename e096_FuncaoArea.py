#  Faça um programa que tenha uma função chamada área(), que receba as
#  dimensões de um terreno retangular (largura e comprimento) e mostre
#  a área do terreno.

def area(larg, comp):
    area = larg * comp
    print(f"Área do terreno: {area:.2f} m²")


def linha():
    print("*-" * 20)


#Programa principal
linha()
print("  >>CALCULADORA DE ÁREA DE TERRENOS<< ")
linha()
l = float(input("Digite a largura do terreno (m): "))
c = float(input("Digite o comprimento do terreno (m): "))
area(l, c)



