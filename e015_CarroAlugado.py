#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro
#  alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a
#  pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print("Vamos calcular o preço do aluguel do veículo.")
km = float(input("Digite a quantidade de quilômetros percorridos: "))
dias = float(input("Digite o número de dias do aluguel: "))
print(f"Valor a pagar = R${(60 * dias) + (0.15 * km):.2f}")
