# Crie um programa onde o usuário digite uma expressão qualquer que use
# parênteses. Seu aplicativo deverá analisar se a expressão passada está
# com os parênteses abertos e fechados na ordem correta.

expressao = str(input("Digite uma expressão matemática, utilizando parênteses: ")).strip().lower()
parenteses_esq = parenteses_dir = 0
for caractere in expressao:
    if caractere == "(":
        parenteses_esq += 1
    if caractere == ")":
        parenteses_dir +=1
if parenteses_esq == parenteses_dir:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está incorreta. Verifique a ordem/quantidade dos parênteses.")

