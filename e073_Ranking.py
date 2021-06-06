# Crie uma tupla preenchida com as 20 primeiras colocadas do
# ranking da WTA, na ordem de colocação. Depois mostre:
# a) As 5 primeiras colocadas.
# b) As 4 últimas colocadas.
# c) Jogadoras em ordem alfabética.
# d) Em que posição está Jennifer Brady.

jogadoras = ('Ashleigh Barty', 'Naomi Osaka', 'Simona Halep',
             'Aryna Sabalenka', 'Sofia Kenin', 'Elina Svitolina',
             'Bianca Andreescu', 'Serena Williams', 'Iga Swiatek',
             'Karolina Pliskova', 'Belinda Bencic', 'Petra Kvitova',
             'Garbiñe Muguruza', 'Jennifer Brady', 'Elise Mertens',
             'Victoria Azarenka', 'Kiki Bertens', 'Maria Sakkari',
             'Karolina Muchova', 'Johanna Konta')
print("\nWTA Ranking - Top 20\n")
pos = 1
for nome in jogadoras:
    print(f"{pos:2} - {nome}")
    pos += 1
print(f"\nAs 5 primeiras colocadas são: {jogadoras[:5]}")
print(f"As 4 últimas colocadas são: {jogadoras[-5:]}")
print(f"Ordem alfabética: {sorted(jogadoras)}")
print(f"Jennifer Brady está na {jogadoras.index('Jennifer Brady') + 1}ª posição.")