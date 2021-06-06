# Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.
celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(f"Convertendo de Celsius para Fahrenheit, temos que:\n{celsius}ºC = {fahrenheit:.1f}ºF.")
