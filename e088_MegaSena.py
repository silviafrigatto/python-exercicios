# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

jogos = []
numeros = []
print("=-" * 25)
print("Bem vindo(a) ao 'Gerador de Jogos da Mega Sena'!")
print("=-" * 25)
while True:
    num_jogos = int(input("Digite o número de jogos: "))
    for jogo in range(0, num_jogos):
        while len(numeros) < 6:
            sorteado = randint(1, 60)
            if sorteado not in numeros:
                numeros.append(sorteado)
        jogos.append(sorted(numeros[:]))
        numeros.clear()
    print()
    for aposta in jogos:
        print(aposta)
    jogos.clear()
    print("\nBOA SORTE!")
    continuar = int(input("\nDigite: 1 para sair - ou - 2 para gerar novos números:"))
    while continuar != 1 and continuar != 2:
        print("Opção inválida.")
        continuar = int(input("\nDigite: 1 para sair - ou - 2 para gerar novos números:"))
    if continuar == 1:
        break







