#  Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
#  diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo
#  e use algumas dessas funções.

import moeda

preco = float(input("Digite o preço: "))
print(moeda.metade(preco))
print(moeda.dobro(preco))
print(moeda.aumentar(preco))
print(moeda.diminuir(preco))
