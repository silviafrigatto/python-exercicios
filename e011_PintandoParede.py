# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
altura = float(input("Digite a altura da parede: "))
largura = float(input("Digite a largura da parede: "))
area = altura * largura
print(f"A área da parede é de {area:.2f}m².\nVocê precisará de {area / 2:.2f} litros de tinta para pintá-la.")
