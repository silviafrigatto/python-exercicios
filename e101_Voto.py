# Crie um programa que tenha uma função chamada voto() que vai receber como
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f"Com {idade} anos: não vota."
    elif 16 >= idade < 18 or idade > 70:
        return f"Com {idade} anos: voto OPCIONAL."
    else:
        return f"Com {idade} anos: voto OBRIGATÓRIO"

ano_nasc = int(input("Digite o ano de nascimento: "))
print(voto(ano_nasc))
