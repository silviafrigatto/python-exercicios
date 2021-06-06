# Crie um programa que tenha uma tupla totalmente preenchida com uma
# contagem por extenso, de zero até vinte. Seu programa deverá ler um
# número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

from time import sleep

extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
print("Olá!")
while True:
    num = int(input("\nDigite um número de 0 a 20: "))
    while num < 0 or num > 20:
        num = int(input("Opção inválida. Digite um número de 0 a 20: "))
    print(f"Você digitou o número {extenso[num]}.")
    continuar = str(input("Deseja continuar? (S / N): ")).strip().upper()[0]
    while continuar not in "SsNn":
        continuar = str(input("Opção inválida. Deseja continuar? (S / N): "))
    if continuar in "Nn":
        print("\nEncerrando...")
        sleep(2)
        break
print("Fim.")

