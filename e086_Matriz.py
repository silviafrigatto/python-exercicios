# Crie um programa que declare uma matriz de dimensão 3×3 e preencha
# com valores lidos pelo teclado. No final, mostre a matriz na tela,
# com a formatação correta.

print("=-" * 20)
print("CRIANDO UMA MATRIZ 3x3")
print("=-" * 20)
matriz = []
valor = 0
i = 0
f = 3
while len(matriz) < 9:
    for linha in range(0, 3):
        for coluna in range(0, 3):
            valor = int(input(f"Digite o valor para a posição {linha},{coluna}: "))
            matriz.append(valor)
while i < 9 and f < 12:
    for num in matriz[i:f]:
        print(f"[{num:^5}]", end="")
    i += 3
    f += 3
    print()







