# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Qual é a velocidade do carro? "))
if velocidade > 80:
    print(f"Limite de velocidade ultrapassado.\nVocê foi multado e deverá pagar R${(velocidade - 80) * 7:.2f}")
else:
    print("A velocidade está dentro do limite.\nBoa viagem!")