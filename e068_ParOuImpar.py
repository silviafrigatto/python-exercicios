#  Faça um programa que jogue par ou ímpar com o computador.
#  O jogo só será interrompido quando o jogador perder, mostrando
#  o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print("=-" * 25)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-" * 25)
vitorias = 0
while True:
    comp = randint(0, 10)
    player = int(input("Digite um número: "))
    escolha = str(input("Escolha par ou ímpar (P / I): ")).strip().upper()[0]
    par_ou_impar = (comp + player) % 2
    while escolha not in "PpIiÍí":
        escolha = str(input("Opção inválida. Escolha par ou ímpar (P / I): ")).strip().upper()[0]
    if par_ou_impar == 0 and escolha in "Pp":
        print(f"O computador escolheu o número {comp}.\nO resultado foi PAR. Você ganhou!")
        print("=-" * 25)
        vitorias += 1
    elif par_ou_impar != 0 and escolha in "IiÍí":
        print(f"O computador escolheu o número {comp}.\nO resultado foi ÍMPAR. Você ganhou!")
        print("=-" * 25)
        vitorias += 1
    else:
        if par_ou_impar == 0 and escolha not in "Pp":
            print(f"O computador escolheu o número {comp}.\nO resultado foi PAR. Você perdeu...")
        if par_ou_impar != 0 and escolha not in "IiÍí":
            print(f"O computador escolheu o número {comp}.\nO resultado foi ÍMPAR. Você perdeu...")
        break
print(f"Total de vitórias: {vitorias}")
print("GAME OVER!")
