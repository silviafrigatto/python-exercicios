# Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Qual é o valor do salário? "))
aumento = salario + (salario * 0.15)
if salario <= 1250:
    print(f"O salário com 15% de aumento é: R${aumento:.2f}")
else:
    aumento = salario + (salario * 0.1)
    print(f"O salário com 10% de aumento é: R${aumento:.2f}")

