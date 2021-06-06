# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando
# os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite o valor da razão: "))
termo = 1
while termo < 11:
    print(primeiro, end=" ")
    primeiro += razao
    termo += 1
