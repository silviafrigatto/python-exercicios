# Faça um programa que leia o ano de nascimento de um jovem e informe, de
# acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print("\033[7mDescubra se você está na idade de se alistar ao serviço militar\033[m")
ano_atual = date.today().year
ano_nasc = int(input("Digite o ano de seu nascimento: "))
idade = ano_atual - ano_nasc
if ano_atual - ano_nasc < 18:
    print(f"Você tem {idade} anos.\nFaltam {18 - idade} anos para você se alistar.")
elif ano_atual - ano_nasc > 18:
    print(f"Você tem {idade} anos.\nVocê passou {idade - 18} anos do prazo para se alistar.")
else:
    print("Você tem 18 anos.\nÉ hora de se alistar!")
