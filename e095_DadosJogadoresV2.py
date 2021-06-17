# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento
# de cada jogador.

from time import sleep

time = list()
while True:
    i = 0
    gols = []
    jogador = {"nome": str(input("\nNome do jogador: ")).strip().upper(),
               "partidas": int(input("Nº de partidas: "))}
    for partida in range(jogador["partidas"]):
        gols.append(int(input(f"- Nº de gols na {partida + 1}ª partida: ")))
    jogador["gols/partida"] = gols
    jogador["total"] = sum(gols)
    print("=-" * 50)
    print(jogador)
    print("=-" * 50)
    print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
    for partida in range(jogador["partidas"]):
        if jogador["gols/partida"][i] == 1:
            print(f'   => Na {partida + 1}ª partida fez {jogador["gols/partida"][i]} gol.')
        else:
            print(f'   => Na {partida + 1}ª partida fez {jogador["gols/partida"][i]} gols.')
        i += 1
    print(f'Total de gols no campeonato: {jogador["total"]}')
    time.append(jogador.copy())
    jogador.clear()
    continuar = str(input("\n- Continuar? [S ou N]: ")).strip().upper()[0]
    while continuar not in "SsNn":
        print("Opção inválida.")
        continuar = str(input("\n- Continuar? [S ou N]: ")).strip().upper()[0]
    if continuar in "Nn":
        break
print()
print("-" * 75)
print(f"{'Nº':<4}{'Nome':<10}{'Gols/partida':<20}{'Total de gols':<20}")
print("-" * 75)
for i, v in enumerate(time):
    print(f"{i + 1:<4}{v['nome']:<10}{str(v['gols/partida']):<20}{str(v['total']):<20}")
print("-" * 75)
codigo = int(input("=> Digite o nº do jogador para ver seu desempenho (999 encerra o programa): "))
for i, v in enumerate(time):
    while codigo == (i + 1):
        print(f'\nO jogador {v["nome"]} jogou {v["partidas"]} partidas.')
        for p, gols in enumerate(v['gols/partida']):
            print(f"   => Total de gols na {p + 1}ª partida: {gols}")
        print(f'Total de gols no campeonato: {v["total"]}')
        print("-" * 75)
        codigo = int(input("\n=> Digite o nº do jogador para ver seu desempenho (999 encerra o programa): "))
        while codigo > len(time):
            print("Opção inválida.")
            codigo = int(input("\n=> Digite o nº do jogador para ver seu desempenho (999 encerra o programa): "))
            if codigo == 999:
                print("\nSaindo...")
                sleep(2)
                break


