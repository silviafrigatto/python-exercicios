# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

from time import sleep

preco = float(input("Digite o valor do produto: R$"))
print('''***Opções de pagamento*** 
1 - À vista em dinheiro/cheque: 10% de desconto
2 - À vista no cartão: 5% de desconto
3 - Em até 2x no cartão: preço formal
4 - 3x ou mais no cartão: 20% de juros''')
opcao = int(input("Digite a opção escolhida: "))
sleep(1)
if opcao == 1:
    pr_desconto = preco - (preco * 0.1)
    print(f"Valor inicial = R${preco:.2f}\nValor à vista (dinheiro/cheque), com 10% de desconto = R${pr_desconto:.2f}")
elif opcao == 2:
    pr_desconto = preco - (preco * 0.05)
    print(f"Valor inicial = R${preco:.2f}\nValor à vista (cartão), com 5% de desconto = R${pr_desconto:.2f}")
elif opcao == 3:
    parcelado = preco / 2
    print(f"Valor inicial = R${preco:.2f}\nValor parcelado em até 2x (cartão) = Duas parcelas de R${parcelado:.2f}")
elif opcao == 4:
    parcelas = int(input("Digite a quantidade de parcelas: "))
    sleep(1)
    pr_juros = preco + (preco * 0.2)
    parcelado = pr_juros / parcelas
    print(f"Valor inicial = R${preco:.2f}\nValor com 20% de juros = R${pr_juros:.2f}\nA ser pago em {parcelas}x de R${parcelado:.2f}")
else:
    print("Opção inválida.")


