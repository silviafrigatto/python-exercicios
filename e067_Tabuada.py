# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando
# o número solicitado for negativo.

while True:
    cont = 1
    num = int(input("Digite um número para ver sua tabuada (ou um número menor ou igual a zero para sair): "))
    if num < 0:
        break
    for operacao in range(1, 11):
        print(f"{num} x {cont:^2} = {num * cont}")
        cont += 1
print("O programa foi encerrado.")



