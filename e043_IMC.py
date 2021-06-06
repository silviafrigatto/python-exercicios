# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
# seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a
# tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

print("***Calculadora de IMC***")
peso = float(input("Peso (em Kg): "))
altura = float(input("Altura (em metros): "))
imc = peso / (pow(altura, 2))
if imc < 18.5:
    print(f"IMC = {imc:.2f}\nIMC abaixo de 18,5: \033[1mAbaixo do Peso\033[m")
elif imc < 25:
    print(f"IMC = {imc:.2f}\nIMC Entre 18,5 e 25: \033[1mPeso Ideal\033[m")
elif imc < 30:
    print(f"IMC = {imc:.2f}\nIMC de 25 até 30: \033[1mSobrepeso\033[m")
elif imc <= 40:
    print(f"IMC = {imc:.2f}\nIMC de 30 até 40: \033[1mObesidade\033[m")
else:
    print(f"IMC = {imc:.2f}\nIMC acima de 40: \033[1mObesidade Mórbida\033[m")


