# Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou
# o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

vencedor = 0
ranking = []
resultados = {"Jogador 1" : randint(1, 6),
              "Jogador 2" : randint(1, 6),
              "Jogador 3" : randint(1, 6),
              "Jogador 4" : randint(1, 6)}
print("=-" * 10)
print("JOGUEM OS DADOS")
print("=-" * 10)
sleep(1)
for k, v in resultados.items():
    print(f"{k} tirou {v}.")
    sleep(1.5)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print("=-" * 10)
print("CLASSIFICAÇÃO FINAL")
print("=-" * 10)
sleep(1)
for i, v in enumerate(ranking):
    print(f"{i + 1}º lugar: {v[0]} com {v[1]} pontos")
    sleep(1.5)
vencedor = ranking[0]
print(f"\n{vencedor[0]} é o vencedor!")


