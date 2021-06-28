def leiaMoeda(msg):
    ok = False
    while not ok:
        entrada = str(input(msg)).replace(",", ".").strip()
        if entrada.isalpha() or entrada == "":
            print("=> ERRO! Digite um preço válido.")
        else:
            ok = True
            return float(entrada)
