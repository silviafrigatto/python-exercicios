#  Crie um programa que tenha uma tupla única com nomes de produtos
#  e seus respectivos preços, na sequência. No final, mostre uma
#  listagem de preços, organizando os dados em forma tabular.

produtos = ('Sorvete', 10.50, 'Hamburger', 15.30,
            'Batata frita', 8.00, 'Suco', 6.80)
itens = produtos[0::2]
precos = produtos[1::2]
cont = 0
print("*" * 52)
print(f"{'PY LANCHES':^50}")
print("*" * 52)
for item in itens:
    print(f"{item:.<30}..............R${precos[cont]:>6.2f}")
    cont += 1