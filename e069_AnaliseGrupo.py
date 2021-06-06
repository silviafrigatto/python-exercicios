# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maiores = homens = mulheres = 0
while True:
    idade = int(input("Idade: "))
    sexo = str(input("Gênero (M / F): ")).strip().upper()[0]
    while sexo not in "MmFf":
        sexo = str(input("Opção inválida. Gênero (M / F): "))
    continuar = str(input("Deseja cadastrar mais uma pessoa? (S / N): ")).strip().upper()[0]
    print("-" * 45)
    while continuar not in "SsNn":
        continuar = str(input("Opção inválida. Deseja cadastrar mais uma pessoa? (S / N): "))
    if idade > 18:
        maiores += 1
    if sexo in "Mm":
        homens += 1
    if sexo in "Ff" and idade < 20:
        mulheres += 1
    if continuar in "Nn":
        break
print(f"- Total de pessoas maiores de 18 anos: {maiores}")
print(f"- Total de homens cadastrados: {homens}")
print(f"- Total de mulheres com menos de 20 anos: {mulheres}")





