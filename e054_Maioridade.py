#  Crie um programa que leia o ano de nascimento de sete pessoas.
#  No final, mostre quantas pessoas ainda não atingiram a maioridade
#  e quantas já são maiores.

from datetime import date

cont_maiores = 0
cont_menores = 0
ano_atual = date.today().year
for num in range(1, 8):
    ano_nasc = int(input("Digite o ano de nascimento: "))
    if ano_atual - ano_nasc >= 18:
        cont_maiores += 1
    else:
        cont_menores += 1
print(f"{cont_maiores} pessoas atingiram a maioridade.")
print(f"{cont_menores} pessoas ainda são menores de 18 anos.")

