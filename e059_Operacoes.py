# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

num_01 = int(input("Digite o primeiro número: "))
num_02 = int(input("Digite o segundo valor: "))
opcao = 0
while opcao != 5:
    print(f"\nVocê digitou os números {num_01} e {num_02}.\nO que deseja fazer com eles?")
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Digitar novos números
[ 5 ] Sair do programa''')
    opcao = int(input("\033[1mDigite a opção desejada: \033[m"))
    if opcao == 1:
        print(f"{num_01} + {num_02} = {num_01 + num_02}")
    elif opcao == 2:
        print(f"{num_01} x {num_02} = {num_01 * num_02}")
    elif opcao == 3:
        if num_01 > num_02:
            print(f"{num_01} é maior que {num_02}.")
        else:
            print(f"{num_02} é maior que {num_01}.")
    elif opcao == 4:
        print("\nDigite dois novos números. ")
        num_01 = int(input("Digite o primeiro número: "))
        num_02 = int(input("Digite o segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
        sleep(2)
    else:
        print("\nOpção inválida. ")
        num_01 = int(input("Digite o primeiro número: "))
        num_02 = int(input("Digite o segundo valor: "))
print("Você saiu do programa.")










