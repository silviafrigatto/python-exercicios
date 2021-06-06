# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

print("Vou pensar em um número entre 0 e 10.")
num_comp = randint(0, 10)
sleep(1)
print("...")
sleep (2)
num_player = int(input("Qual número eu pensei? "))
tentativas = 1
while num_player != num_comp:
    num_player = int(input(f"Hmm...Não pensei no número {num_player}... Tente outra vez: "))
    tentativas += 1
    if num_player == num_comp:
        print(f"Você acertou! Eu pensei no número {num_comp}.")
        print(f"Você precisou de {tentativas} tentativas para acertar.")