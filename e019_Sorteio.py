# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela
# o nome do escolhido.

from random import choice
print("Digite o nome dos alunos:")
aluno01 = str(input("Aluno 1: "))
aluno02 = str(input("Aluno 2: "))
aluno03 = str(input("Aluno 3: "))
aluno04 = str(input("Aluno 4: "))
print(f"O aluno sorteado foi: {choice([aluno01, aluno02, aluno03, aluno04])}.")

