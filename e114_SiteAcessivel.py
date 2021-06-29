# Crie um código em Python que teste se o site pudim está acessível pelo
# computador usado.

import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen("http://pudim.com.br/")
except urllib.error.URLError:
    print('O site não está disponível :(')
else:
    print('O site foi acessado com sucesso!')
