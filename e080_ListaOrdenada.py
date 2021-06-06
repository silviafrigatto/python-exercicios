#  Crie um programa onde o usuário possa digitar cinco valores numéricos
#  e cadastre-os em uma lista, já na posição correta de inserção
#  (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for pos in range(0, 5):
    valor = int(input(f"Digite o {pos + 1}º número: "))
    if pos == 0 or valor > lista[-1]:
        lista.append(valor)
        print(f"O valor {valor} foi adicionado ao final da lista.")
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f"O valor {valor} foi adicionado à posição {pos + 1}.")
                break
            pos += 1
print(f"Foram digitados os números {lista}")

