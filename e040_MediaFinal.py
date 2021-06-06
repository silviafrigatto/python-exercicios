# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2
if media < 5:
    print(f"A média final foi {media}\nMédia abaixo de 5.0: REPROVADO")
elif media >= 7:
    print(f"A média final foi {media}\nMédia 7.0 ou superior: APROVADO")
else:
    print(f"A média final foi {media}\nMédia entre 5.0 e 6.9: RECUPERAÇÃO")