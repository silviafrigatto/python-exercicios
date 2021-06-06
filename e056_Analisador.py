#  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#  No final do programa, mostre: a média de idade do grupo, qual é o nome
#  do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idades = 0
velho = 0
novo = 0
menos_20 = 0
nome_velho = ""
nome_novo = ""
for pessoa in range(1, 5):
    print(f"\033[1mDados da {pessoa}ª pessoa\033[m")
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (M/F): ")).strip().upper()
    print("*" * 20)
    soma_idades += idade  # Para verificar a média de idades
    # Verificar quem é o homem mais novo e quem é o mais velho
    if pessoa == 1:
        velho = idade
        novo = idade
    else:
        if idade > velho and sexo == "M":
            velho = idade
            nome_velho = nome
        if idade < novo and sexo == "M":
            novo = idade
            nome_novo = nome
    # Verificar quantas mulheres têm menos de 20 anos
    if sexo == "F" and idade < 20:
        menos_20 += 1
print(f"A média de idade desse grupo é de {soma_idades / 4:.1f} anos.")
print(f"{nome_novo} é o homem mais novo e tem {novo} anos.")
print(f"{nome_velho} é o homem mais velho e tem {velho} anos.")
print(f"Número de mulheres com menos de 20 anos: {menos_20}")





