# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print("Deu erro")
else:
    print("Tudo ok")
    print(site.read().decode('utf-8'))