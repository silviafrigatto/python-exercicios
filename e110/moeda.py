#  Módulo criado para o exercício 110.


def aumentar(valor, taxa=0, formatado=False):
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
    else:
        return aumento


def diminuir(valor, taxa=0, formatado=False):
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
    else:
        return desconto


def dobro(valor, formatado=False):
    '''
    => Função que calcula o dobro de um valor.
    :param valor: Valor a ser dobrado.
    :param formatado: Formata os valores como monetários
    :return: Retorna o dobro do valor informado
    '''
    dobrar = valor * 2
    if formatado:
        return moeda(dobrar)
    else:
        return dobrar


def metade(valor, formatado=False):
    '''
    => Função que calcula a metade de um valor.
    :param valor: Valor a ser dividido.
    :param formatado: Formata os valores como monetários
    :return: Retorna a metade do valor informado
    '''
    dividir = valor / 2
    if formatado:
        return moeda(dividir)
    else:
        return dividir


def moeda(valor=0, cifra="R$"):
    '''
    => Função que formata valores como monetários.
    :param valor: Valor a ser formatado.
    :param cifra: Tipo de moeda.
    :return: Retorna o valor em formato monetário.
    '''
    return f"{cifra}{valor:.2f}".replace(".", ",")


def titulo(msg):
    print("-" * 30)
    print(f"{msg.center(30)}")
    print("-" * 30)


def resumo(valor=0, aumento=10, desconto=5):
    titulo("RESUMO DO VALOR")
    print(f"Preço analisado: \t{moeda(valor)}")
    print(f"Metade do preço: \t{metade(valor, True)}")
    print(f"Dobro do preço: \t{dobro(valor, True)}")
    print(f"{aumento}% de aumento: \t{aumentar(valor, aumento, True)}")
    print(f"{desconto}% de desconto: \t{diminuir(valor, desconto, True)}")
    print("-" * 30)
