# Crie um programa onde o usuário digite uma expressão qualquer que use
# parênteses. Seu aplicativo deverá analisar se a expressão passada está
# com os parênteses abertos e fechados na ordem correta.

expressao = str(input("Digite uma expressão matemática, utilizando parênteses: ")).strip().lower()
parenteses = []
for caractere in expressao:
    if caractere == "(":
        parenteses.append(caractere)
    if caractere == ")":
        parenteses.pop()
if len(parenteses) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está incorreta. Verifique a ordem/quantidade dos parênteses.")

