# Crie um programa que leia nome e duas notas de vários alunos e guarde
# tudo em uma lista composta. No final, mostre um boletim contendo a média
# de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

from time import sleep

alunos = []
while True:
    nome = str.title(input("Nome do aluno: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, nota1, nota2, media])
    continuar = str(input("- Continuar? [S/N]: ")).strip().upper()[0]
    while continuar not in "SsNn":
        print("Opção inválida.")
        continuar = str(input("- Continuar? [S/N]: ")).strip().upper()[0]
    if continuar in "Nn":
        break
print("-" * 30)
print(f"{'Nº':<4}{'Nome':<10}{'Nota':>8}")
print("-" * 30)
for aluno in alunos:
    print(f"{alunos.index(aluno) + 1:<4}{aluno[0]:<10}{aluno[3]:>8}")
print("-" * 30)
codigo = int(input("Digite o nº do aluno para ver suas notas (999 encerra o programa): "))
for aluno in alunos:
    while codigo == alunos.index(aluno) + 1:
        print(f"Notas de {aluno[0]}: {aluno[1:3]}")
        codigo = int(input("\nDigite o nº do aluno para ver suas notas (999 encerra o programa): "))
        while codigo > len(alunos):
            print("Opção inválida.")
            codigo = int(input("\nDigite o nº do aluno para ver suas notas (999 encerra o programa): "))
            if codigo == 999:
                print("Saindo...")
                sleep(2)
                break









