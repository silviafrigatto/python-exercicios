# Escreva um programa em Python que leia um número inteiro qualquer e peça
# para o usuário escolher qual será a base de conversão: 1 para binário, 2
# para octal e 3 para hexadecimal.

print("\033[7mBem vindo ao conversor de bases numéricas!\033[m")
num = int(input("Digite um número: "))
print('''Escolha uma opção:
1 - Para converter o número para BINÁRIO
2 - Para converter o número para OCTAL
3 - Para converter o número para HEXADECIMAL''')
opcao = int(input("Digite a opção escolhida: "))

if opcao == 1:
    print(f"O número {num} em BINÁRIO é: {bin(num)[2:]}")
elif opcao == 2:
    print(f"O número {num} em OCTAL é: {oct(num)[2:]}")
elif opcao == 3:
    print(f"O número {num} em HEXADECIMAL é: {hex(num)[2:]}")
else:
    print("Opção inválida. Tente novamente.")
