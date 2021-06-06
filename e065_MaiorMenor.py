# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual
# foi o maior e o menor valores lidos. O programa deve perguntar ao
# usuário se ele quer ou não continuar a digitar valores.

print("=-" * 30)
num = float(input("Digite um número: "))
continuar = str(input("Deseja digitar mais um número? [S / N]: ")).strip().upper()[0]
soma = maior = menor = num
total_num = 1
while continuar not in "Nn":
    print("=-" * 30)
    num = float(input("Digite um número: "))
    continuar = str(input("Deseja digitar mais um número? [S / N]: ")).strip().upper()[0]
    soma += num
    total_num += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    while continuar not in "SsNn":
        continuar = str(input("Opção inválida. Digite novamente [S / N]: "))
print("=-" * 30)
print(f"Você digitou {total_num} números.")
print(f"- A soma entre eles é igual a {soma:.0f}")
print(f"- A média dos valores é igual a {soma / total_num:.1f}")
print(f"- Maior número: {maior:.0f}\n- Menor número: {menor:.0f}")




