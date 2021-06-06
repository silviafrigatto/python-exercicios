# Crie um programa que leia uma frase qualquer e diga se ela é um
# palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA.

frase = str(input("Digite uma frase: ")).strip().upper().split()
palavras_juntas = "".join(frase)
for letra in palavras_juntas.split():
    print(letra[0:])
    print(letra[::-1])
    if letra[0:] == letra[::-1]:
        print(f'"{" ".join(frase)}" é um palíndromo.')
    else:
        print(f'"{" ".join(frase)}" não é palíndromo.')



