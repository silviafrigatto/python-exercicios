# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print("Vamos jogar \033[1;35mJokenpô\033[m! Será que você consegue ganhar do computador?")
print('''Escolha a opção:
1 - Tesoura
2 - Papel
3 - Pedra''')
jogador = int(input("Digite o número da opção escolhida: "))
computador = randint(1,3)
itens = ('PEDRA', 'PAPEL', 'TESOURA')
ganhou = "PARABÉNS! VOCÊ GANHOU!"
perdeu = "QUE PENA...VOCÊ PERDEU."
sleep(0.5)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!")
print("=-" * 40)
print(f"Você jogou {itens[jogador]}.")
print(f"Computador jogou {itens[computador]}.")
print("=-" * 40)
#Possibilidades do jogador vencer
if jogador == 1 and computador == 2:
    print(ganhou)
elif jogador == 2 and computador == 3:
    print(ganhou)
elif jogador == 3 and computador == 1:
    print(ganhou)
#Possibilidades do jogador perder
elif jogador == 1 and computador == 3:
    print(perdeu)
elif jogador == 2 and computador == 1:
    print(perdeu)
elif jogador == 3 and computador == 2:
    print(perdeu)
#Possibilidades de empate
else:
    print("EMPATOU!")

