#  Módulo criado para o exercício 108.
#  Exercicio 108: Adapte o código do desafio #107, criando uma função adicional
#  chamada moeda() que consiga mostrar os números como um valor monetário formatado.

def aumentar(valor, taxa):
    '''
    => Função que calcula um valor com aumento.
    :param valor: Valor informado pelo usuário.
    :param taxa: Taxa de aumento (Ex.: Para calcular um aumento de 10%, digitar 10.
    :return: Retorna o valor acrescido do aumento.
    '''
    aumento = valor + (valor * (taxa / 100))
    return aumento


def diminuir(valor, taxa):
    '''
    => Função que calcula um valor com desconto.
    :param valor: Valor informado pelo usuário.
    :param taxa: Taxa de desconto (Ex.: Para calcular um desconto de 10%, digitar 10.
    :return: Retorna o valor com o desconto.
    '''
    desconto = valor - (valor * (taxa / 100))
    return desconto


def dobro(valor):
    '''
    => Função que calcula o dobro de um valor.
    :param valor: Valor a ser dobrado.
    :return: Retorna o dobro do valor informado
    '''
    return valor * 2


def metade(valor):
    '''
    => Função que calcula a metade de um valor.
    :param valor: Valor a ser dividido.
    :return: Retorna a metade do valor informado
    '''
    return valor / 2


def moeda(valor=0, moeda="R$"):
    return f"{moeda}{valor:.2f}".replace(".", ",")

