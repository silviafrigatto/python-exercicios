# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado
# (número inteiro) e o programa vai informar quantas cédulas de cada
# valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cont_50 = cont_20 = cont_10 = cont_1 = 0
while True:
    print("Bem vindo(a) ao serviço de caixa eletrônico do Banco Py")
    valor = int(input("Digite o valor a ser sacado: "))
    while valor > 0:
        if valor >= 50:
            cont_50 += 1
            valor -= 50
        if 20 <= valor < 50:
            cont_20 += 1
            valor -= 20
        if 10 <= valor < 20:
            cont_10 += 1
            valor -= 10
        if 1 <= valor < 10:
            cont_1 += 1
            valor -= 1
    if valor == 0:
        break
print("Você receberá:")
print(f"- {cont_50} notas de R$50.00")
print(f"- {cont_20} notas de R$20.00")
print(f"- {cont_10} notas de R$10.00")
print(f"- {cont_1} notas de R$1.00")



