# Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com o nome “SANTO”.

cidade = str(input("Digite o nome da cidade: ")).strip().upper()
print(f"O nome da cidade começa com SANTO?", cidade[:5] == "SANTO")