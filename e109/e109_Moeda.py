#  Modifique as funções que form criadas no desafio 107 para que elas aceitem
#  um parâmetro a mais, informando se o valor retornado por elas vai ser ou não
#  formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

preco = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}")
print(f"O valor de {moeda.moeda(preco)} com aumento de 10% é {moeda.aumentar(preco, 10, True)}")
print(f"O valor de {moeda.moeda(preco)} com desconto de 10% é {moeda.diminuir(preco, 10, True)}")
