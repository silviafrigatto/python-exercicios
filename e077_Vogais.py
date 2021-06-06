# Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais são as suas vogais.

print("Digite 5 palavras - não colocar acentos")
palavras = (str(input("1ª palavra: ")).strip().upper(),
            str(input("2ª palavra: ")).strip().upper(),
            str(input("3ª palavra: ")).strip().upper(),
            str(input("4ª palavra: ")).strip().upper(),
            str(input("5ª palavra: ")).strip().upper())
for palavra in palavras:
    print(f"\nA palavra {palavra} tem as vogais: ", end="")
    for letra in palavra:
        if letra in "AaEeIiOoUu":
            print(letra, end=" ")



