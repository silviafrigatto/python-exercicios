# Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com o nome “SANTO”.

# .strip() Retira espaços do começo e do final da string;
# .upper() Transforma todas as letras em maiúsculas;
# .split() Cria uma lista com as palavras digitadas.
nome = str(input("Digite o nome da cidade: ")).strip().upper().split()
print(f"O nome da cidade começa com SANTO?", "SANTO" in nome[0])


