# Escreva um programa que leia um número N inteiro qualquer e mostre na
# tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

print("=-" * 21)
print("Sequência de Fibonacci")
print("=-" * 21)
termos = int(input("Digite o número de elementos da sequência: "))
t1 = 0
t2 = 1
cont_termos = 3
print(t1, t2, end=" ")
while cont_termos <= termos:
    t3 = t1 + t2
    print(t3, end=" ")
    t1 = t2
    t2 = t3
    cont_termos += 1


