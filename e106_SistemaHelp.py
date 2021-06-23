#  Faça um mini-sistema que utilize o Interactive Help do Python.
#  O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário
#  digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.


from time import sleep


c = ("\033[m",            # - sem cor
     "\033[0;30;41m",     # - vermelho
     "\033[7;30;42m",     # - verde
     "\033[0;30;43m",     # - amarelo
     "\033[0;30;44m",     # - azul
     "\033[0;30;45m",     # - roxo
     "\033[7;40m"         # - branco
     )

def titulo(msg, cor=0):
    tamanho = len(msg) + 2
    print(c[cor], end="")
    print("~" * tamanho)
    print(f" {msg}")
    print("~" * tamanho)
    print(c[0], end="")
    sleep(1)


def manual(comando):
    titulo(f"Acessando o manual do comando {comando}", 4)
    print(c[6], end="")
    help(comando)
    print(c[0], end="")
    sleep(2)


while True:
    titulo("SISTEMA DE AJUDA PYHELP", 2)
    pesquisar = str(input("Função ou biblioteca: "))
    if pesquisar.strip().upper() == "FIM":
        titulo("ATÉ LOGO!", 1)
        break
    else:
        manual(pesquisar)