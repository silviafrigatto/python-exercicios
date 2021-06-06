# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

lista = []
repetidas = []
while True:
    num = lista.append(int(input("\nDigite um número: ")))
    continuar = str(input("Deseja continuar? [S / N]: ")).strip().upper()[0]
    if continuar not in "SsNn":
        continuar = str(input("Opção inválida. Digite S ou N: "))
    if continuar in "Nn":
        break
print(f"\nOs números digitados foram: {lista}")
for elemento in lista:
    if elemento not in repetidas:
        repetidas.append(elemento)
print(f"Valores únicos digitados e em ordem crescente: {sorted(repetidas)}")



