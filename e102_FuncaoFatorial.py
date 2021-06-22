# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um
# valor lógico (opcional) indicando se será mostrado ou não na tela o processo
# de cálculo do fatorial.

def fatorial(num, show=False):
    '''
    Calcula o fatorial de um número indicado pelo usuário.
    :param num: número a ser calculado.
    :param show: dá a opção de mostrar ou não o cálculo.
    :return: retorna o fatorial do número.
    '''
    from math import factorial
    for valor in range(num, 0, -1):
        if show:
            print(valor, end="")
            if valor > 1:
                print(f" x ", end="")
            else:
                print(f" = ", end="")
    return f"{factorial(num)}"


help(fatorial)
n = int(input("Calcule o fatorial de: "))
print(fatorial(n, show=True))

