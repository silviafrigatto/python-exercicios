# Escreva um programa para aprovar o empréstimo bancário para a compra de
# uma casa. Pergunte o valor da casa, o salário do comprador e em quantos
# anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
# ou então o empréstimo será negado.

print("\033[7mAnalisador de empréstimos\033[m")
valor_casa = float(input("- Valor da casa: R$"))
salario_mes = float(input("- Salário do comprador: R$"))
anos = float(input("- Em quantos anos irá pagar: "))
meses = anos * 12
if valor_casa / meses > salario_mes * 0.3:
    print(f"\033[1mValor da prestação:\033[m R${valor_casa / meses:.2f}\nEmpréstimo \033[1;31mNEGADO\033[m.")
else:
    print(f"Valor da prestação: R${valor_casa / meses:.2f}\nEmpréstimo \033[1;32mAPROVADO\033[m.")