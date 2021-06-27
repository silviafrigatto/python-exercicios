#  Módulo criado para o exercício 108.
#  Exercicio 108: Adapte o código do desafio #107, criando uma função adicional
#  chamada moeda() que consiga mostrar os números como um valor monetário formatado.

def aumentar(valor, taxa, formatado=False):
    '''
    => Função que calcula um valor com aumento.
    :param valor: Valor informado pelo usuário.
    :param taxa: Taxa de aumento (Ex.: Para calcular um aumento de 10%, digitar 10.
    :param formatado: Formata os valores como monetários
    :return: Retorna o valor acrescido do aumento.
    '''
    aumento = valor + (valor * (taxa / 100))
    if formatado:
        return moeda(aumento)
    return aumento


def diminuir(valor, taxa, formatado=False):
    '''
    => Função que calcula um valor com desconto.
    :param valor: Valor informado pelo usuário.
    :param taxa: Taxa de desconto (Ex.: Para calcular um desconto de 10%, digitar 10.
    :param formatado: Formata os valores como monetários
    :return: Retorna o valor com o desconto.
    '''
    desconto = valor - (valor * (taxa / 100))
    if formatado:
        return moeda(desconto)
    return desconto


def dobro(valor, formatado=False):
    '''
    => Função que calcula o dobro de um valor.
    :param valor: Valor a ser dobrado.
    :param formatado: Formata os valores como monetários
    :return: Retorna o dobro do valor informado
    '''
    dobro = valor * 2
    if formatado:
        return moeda(dobro)
    return dobro


def metade(valor, formatado=False):
    '''
    => Função que calcula a metade de um valor.
    :param valor: Valor a ser dividido.
    :param formatado: Formata os valores como monetários
    :return: Retorna a metade do valor informado
    '''
    metade = valor / 2
    if formatado:
        return moeda(metade)
    return metade



def moeda(valor=0, moeda="R$"):
    return f"{moeda}{valor:.2f}".replace(".", ",")

