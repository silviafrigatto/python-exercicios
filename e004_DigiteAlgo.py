# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo,
# e todas as informações possíveis sobre ele.
algo = input("Digite algo: ")
print(f"O tipo primitivo de {algo} é: ", type(algo))
print(f"{algo} é alfanumérico? ", algo.isalnum())
print(f"{algo} é numérico? ", algo.isnumeric())
print(f"{algo} é alfabético? ", algo.isalpha())
print(f"{algo} tem somente letras minúsculas? ", algo.islower())
print(f"{algo} tem somente letras maiúsculas? ", algo.isupper())
