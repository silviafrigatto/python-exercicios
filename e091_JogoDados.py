# Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou
# o maior número no dado.

from random import randint
from time import sleep

resultados = {"Jogador 1" : randint(1, 6),
              "Jogador 2" : randint(1, 6),
              "Jogador 3" : randint(1, 6),
              "Jogador 4" : randint(1, 6)}
cont = 1
print("=-" * 10)
print("JOGUEM OS DADOS")
print("=-" * 10)
sleep(1)
for k, v in resultados.items():
    print(f"{k} tirou {v}.")
    sleep(1.5)
ordem = dict(sorted(resultados.items(), key=lambda x: x[1], reverse=True))
print("=-" * 10)
print("CLASSIFICAÇÃO FINAL")
print("=-" * 10)
sleep(1)
for k, v in ordem.items():
    print(f"{cont}º lugar: {k}")
    cont += 1
    sleep(1.5)
vencedor = max(ordem, key=lambda x: x[1])
print(f"\n{vencedor} é o vencedor!")



