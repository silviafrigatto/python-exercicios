# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista_A = []
lista_B = []
lista_C = []
while True:
    valor = lista_A.append(int(input("Digite um número: ")))
    continuar = str(input("- Deseja continuar? [S/N]: ")).strip().upper()[0]
    while continuar not in "SsNn":
        continuar = str(input("- Opção inválida. Digite S para 'sim' ou N para 'nao': "))
    if continuar in "Nn":
        break
for elemento in lista_A:
    if elemento % 2 == 0:
        lista_B.append(elemento)
    else:
        lista_C.append(elemento)
print("*" * 50)
print(f"Lista de números digitados: {sorted(lista_A)}")
print(f"Lista de números pares: {sorted(lista_B)}")
print(f"Lista de números ímpares: {sorted(lista_C)}")
print(f"Lista com todos os valores: {sorted(lista_A) + sorted(lista_B) + sorted(lista_C)}")


