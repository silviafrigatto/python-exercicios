# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input("Digite o valor em metros: "))
dm = m * 10
cm = m * 100
mm = m * 1000
dam = m / 10
hm = m / 100
km = m / 1000
print(f"{m} m equivale a:\n{dm} dm\n{cm} cm\n{mm} mm\n{dam} dam\n{hm} hm\n{km} km")
