# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    valor = lista.append(int(input("Digite um número: ")))
    continuar = str(input("- Deseja continuar? [S/N]: ")).strip().upper()[0]
    while continuar not in "SsNn":
        continuar = str(input("- Opção inválida. Digite S para 'sim' ou N para 'nao': "))
    if continuar in "Nn":
        break
print("*" * 50)
lista.sort(reverse=True)
print(f"Total de números digitados: {len(lista)}")
print(f"Números digitados em ordem decrescente: {lista}")
print("O número 5 está na lista?", end=" ")
if 5 in lista:
    print("Sim")
else:
    print("Não")



