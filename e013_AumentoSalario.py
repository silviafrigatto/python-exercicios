# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.
salario = float(input("Digite o salário: R$"))
aumento = 15 / 100
print(f"O valor do salário com 15% de aumento é R${salario + (salario * aumento):.2f}.")
