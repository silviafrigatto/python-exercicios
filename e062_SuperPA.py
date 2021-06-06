#  Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar
#  mais alguns termos. O programa encerrará quando ele disser que quer
#  mostrar 0 termos.

primeiro = int(input("\033[1mDigite o primeiro termo da PA: \033[m"))
razao = int(input("\033[1mDigite o valor da razão: \033[m"))
termo_init = 1
while termo_init < 11:  # Enquanto o número de termos for menor que 11 (para mostrar até o décimo termo)
    print(primeiro, end=" ")  # Imprime o valor do primeiro termo
    primeiro += razao  # Adiciona o valor da razão ao termo
    termo_init += 1  # Adiciona 1 ao contador de termos
termo_add = int(input("\n\033[1mQuantos termos você deseja ver a mais? \033[m"))
termo_init = 1
while termo_add != 0:
    termo_init = 1
    while termo_init < termo_add + 1:
        print(primeiro, end=" ")
        primeiro += razao
        termo_init += 1
    termo_add = int(input("\n\033[1mQuantos termos você deseja ver a mais? \033[m"))
print("\033[1mFIM\033[m")






