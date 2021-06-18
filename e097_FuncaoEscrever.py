# Faça um programa que tenha uma função chamada escreva(), que receba
# um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(string):
    tamanho = len(string)
    print("-" * tamanho)
    print(string)
    print("-" * len(string))


escreva("HELLO, UNIVERSO!")
escreva("OLÁ, MUNDO!")
escreva("ESTOU ADORANDO APRENDER PYTHON!")




