#  Módulo criado para o exercício 107.

def aumentar(valor):
    aumento = valor + (valor * 0.1)
    return f"Com aumento de 10%, temos R${aumento}"


def diminuir(valor):
    desconto = valor - (valor * 0.1)
    return f"Com desconto de 10%, temos R${desconto}"


def dobro(valor):
    return f"O dobro de R${valor} é R${valor * 2}"


def metade(valor):
    return f"A metade de R${valor} é R${valor / 2}"

