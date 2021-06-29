# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
# possibilidade da digitação de um número de tipo inválido. Aproveite e crie
# também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(valor):
    while True:
        try:
            inteiro = int(input(valor))
        except:
            print("\033[31mErro => Você não digitou um \033[1;31mint\033[m \033[m")
        else:
            return inteiro


def leiaFloat(valor):
    while True:
        try:
            valor_float = float(input(valor))
        except:
            print("\033[31mErro => Você não digitou um \033[1;31mfloat\033[m \033[m")
        else:
            return valor_float


n1 = leiaInt('Digite um valor do tipo \033[33mint\033[m: ')
n2 = leiaFloat('Digite um valor do tipo \033[34mfloat\033[m: ')
print(f'=> {n1} é \033[33mint\033[m')
print(f'=> {n2} é \033[34mfloat\033[m')





