# Faça um programa que leia nome e média de um aluno, guardando também a
# situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno["Nome"] = str.title(input("Nome do aluno: ")).strip()
aluno["Média"] = float(input("Média: "))
if aluno["Média"] >= 7:
    aluno["Situação"] = "Aprovado"
elif 5 <= aluno["Média"] < 7:
    aluno["Situação"] = "Recuperação"
else:
    aluno["Situação"] = "Reprovado"
print("=-" * 20)
for k, v in aluno.items():
    print(f"{k}: {v}")

