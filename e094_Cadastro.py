# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários
# em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = list()
mulheres = list()
cadastro = dict()
soma = media = 0
while True:
    cadastro['nome'] = str(input("Nome: ")).strip().upper()
    cadastro['sexo'] = str(input("Sexo [M ou F]: ")).strip().upper()[0]
    while cadastro['sexo'] not in "MmFf":
        print("Opção inválida.")
        cadastro['sexo'] = str(input("Sexo [M ou F]: ")).strip().upper()[0]
    cadastro['idade'] = int(input("Idade: "))
    soma += cadastro['idade']
    pessoas.append(cadastro.copy())
    if cadastro['sexo'] in "Ff":
        mulheres.append(cadastro.copy())
    cadastro.clear()
    continuar = str(input("- Continuar? [S ou N]: ")).strip().upper()[0]
    while continuar not in "SsNn":
        print("Opção inválida.")
        continuar = str(input("- Continuar? [S ou N]: ")).strip().upper()[0]
    if continuar in "N":
        break
print("=-" * 30)
media = soma / len(pessoas)
print(f"Total de pessoas cadastradas: {len(pessoas)}")
print(f"Média de idade: {media:.0f} anos")
print("Mulheres cadastradas:")
for mulher in mulheres:
    print(f"- {mulher['nome']}")
print(f"Pessoas com idade acima da média:")
for cadastro in pessoas:
    if cadastro['idade'] > media:
        print(f"- {cadastro['nome']}")








