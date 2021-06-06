#  Faça um programa que leia o nome completo de uma pessoa, mostrando
#  em seguida o primeiro, o último nome e os nomes do meio separadamente.

nome = str(input("Digite o nome completo: ")).strip().split()
print(f"Nome completo: ", " ".join(nome))
print(f"Primeiro nome: ", nome[0])
print(f"Último nome: ", nome[-1])
print(f"Nomes intermediários: ", " ".join(nome[1:-1]))
