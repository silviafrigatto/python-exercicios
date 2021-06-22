# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
# opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser
# capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado
# corretamente.

def ficha(nome="", gols=0):
   return f"O jogador {nome} marcou {gols} gols(s) no campeonato."


n = str.title(input("Nome do jogador: ")).strip()
g = str(input("Total de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = "---"
if n.isalpha() == False:
    n = "<não informado>"


print(ficha(n, g))

