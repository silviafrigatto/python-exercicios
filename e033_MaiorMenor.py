# Faça um programa que leia três números e mostre qual é o maior e qual
# é o menor.

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
if n1 > n2 and n2 > n3:
    print(f"O maior número é {n1}.\nO menor número é {n3}.")
elif n1 > n3 and n3 > n2:
    print(f"O maior número é {n1}.\nO menor número é {n2}")
elif n2 > n1 and n1 > n3:
    print(f"O maior número é {n2}.\nO menor número é {n3}.")
elif n2 > n3 and n3 > n1:
    print(f"O maior número é {n2}.\nO menor número é {n1}.")
elif n3 > n1 and n1 > n2:
    print(f"O maior número é {n3}.\nO menor número é {n2}.")
else:
    print(f"O maior número é {n3}.\nO menor número é {n1}.")
