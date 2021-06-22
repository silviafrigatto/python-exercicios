# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
# semelhante ‘a função input() do Python, só que fazendo a validação para
# aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):
    while True:
        msg = str(input("Digite um número: "))
        while msg.isnumeric() == False:
            print(f"\033[0;31m=> ERRO! O valor digitado não é numérico.\033[m")
            msg = str(input("Digite um número: "))
        if msg.isnumeric():
            print(f"\033[0;32m=> {msg} é um valor numérico.\033[m")
            break


n = str(leiaInt("Digite um número: "))

