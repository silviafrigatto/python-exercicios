#  Escreva um programa que faça o computador “pensar” em um número inteiro
#  entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
#  pelo computador. O programa deverá escrever na tela se o usuário venceu ou
#  perdeu.

import random
print("=-" * 30)
print("Tente adivinhar o número que o computador escolheu.")
print("=-" * 30)
num_comp = random.randint(0, 5)
num_user = int(input("Digite um número de 0 a 5: "))
print(f"O número que o computador escolheu foi: {num_comp}.")
if num_user == num_comp:
    print("Parabéns! Você venceu.")
else:
    print("Que pena, você perdeu.")
