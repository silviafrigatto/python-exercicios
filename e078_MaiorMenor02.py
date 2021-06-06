# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.

lista = []
for pos in range(0, 5):
    lista.append(int(input(f"Digite um número para a {pos + 1}ª posição: ")))
print(f"Você digitou os seguintes valores: {sorted(lista)}")
print(f"\nO menor número digitado foi {min(lista)}, na posição ", end="")
for pos, valor in enumerate(lista):
    if valor == min(lista):
        print(f"{pos + 1}", end=" ")
print(f"\nO maior número digitado foi {max(lista)}, na posição ", end="")
for pos, valor in enumerate(lista):
    if valor == max(lista):
        print(f"{pos + 1}", end=" ")