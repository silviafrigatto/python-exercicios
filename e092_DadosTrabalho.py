# Crie um programa que leia nome, ano de nascimento e carteira de
# trabalho e cadastre-o (com idade) em um dicionário. Se por acaso
# a CTPS for diferente de ZERO, o dicionário receberá também o ano
# de contratação e o salário. Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar (considerar 35 anos
# de contribuição).

from datetime import date

cadastro = {"Nome": str.title(input("Nome: ")).strip(),
            "Idade": int(input("Ano de nascimento: ")),
            "Carteira": int(input("Carteira de trabalho (0 se não tiver): "))}
if cadastro["Carteira"] != 0:
    cadastro["Ano de contratação"] = int(input("Ano de contratação: "))
    cadastro["Salário"] = float(input("Salário: "))
    cadastro["Idade de aposentadoria"] = (cadastro["Ano de contratação"] - cadastro["Idade"]) + 35
    cadastro["Idade"] = date.today().year - cadastro["Idade"]
    print("=-" * 30)
    for k, v in cadastro.items():
        print(f"- {k}: {v}")
else:
    print("=-" * 30)
    for k, v in cadastro.items():
        cadastro["Idade"] = date.today().year - cadastro["Idade"]
        print(f"- {k}: {v}")







