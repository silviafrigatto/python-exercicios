# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total
# de gols feitos durante o campeonato.

i = 0
gols = []
jogador = {"nome": str(input("Nome do jogador: ")).strip().upper(),
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











