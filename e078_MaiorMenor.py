# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.

valores = (int(input("Digite um valor para a 1ª posição: ")),
           int(input("Digite um valor para a 2ª posição: ")),
           int(input("Digite um valor para a 3ª posição: ")),
           int(input("Digite um valor para a 4ª posição: ")),
           int(input("Digite um valor para a 5ª posição: ")))
lista = list(sorted(valores))
print(f"\nO menor número digitado foi {min(lista)}, na posição ", end="")
for pos, valor in enumerate(lista):
    if valor == min(lista):
        print(f"{pos + 1}", end=" ")
print(f"\nO maior número digitado foi {max(lista)}, na posição ", end="")
for pos, valor in enumerate(lista):
    if valor == max(lista):
        print(f"{pos + 1}", end=" ")
