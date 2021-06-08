#  Aprimore o desafio anterior, mostrando no final:
#  A) A soma de todos os valores pares digitados.
#  B) A soma dos valores da terceira coluna.
#  C) O maior valor da segunda linha.

print("=-" * 20)
print("CRIANDO UMA MATRIZ 3x3")
print("=-" * 20)
matriz = []
i = valor = soma_pares = soma_coluna = 0
f = 3
while len(matriz) < 9:
    for linha in range(0, 3):
        for coluna in range(0, 3):
            valor = int(input(f"Digite o valor para a posição {linha},{coluna}: "))
            if valor % 2 == 0:
                soma_pares += valor
            matriz.append(valor)
while i < 9 and f < 12:
    for num in matriz[i:f]:
        print(f"[{num:^5}]", end="")
    i += 3
    f += 3
    print()
print(f"Soma dos números pares: {soma_pares}")
for num in range(matriz[2], len(matriz) + 1, 3):
    soma_coluna += num
print(f"Soma dos valores da terceira coluna: {soma_coluna}")
sorted(matriz[3:6])
print(f"O maior valor da segunda linha é: {max(matriz[3:6])}")


