import os
from socket import *

nomeServidor = '192.0.2.10'

portaServidor = 12000

socketCliente = socket (AF_INET, SOCK_STREAM)

socketCliente.connect ((nomeServidor, portaServidor))

request = "GET / HTTP/1.1\nHost: boasvindas.ufs \nAccept-Language: pt-br"

socketCliente.send (request.encode())

print "Recebendo pagina de boas vindas"

arq = open('/tmp/20211-lab-t2-jvarodrigues/assets/boasvindas.html', 'w')

while 1:
    dados = socketCliente.recv(1024)
    if not dados:
        break
    arq.write(dados)
    
arq.close()

socketCliente.close ()

os.system("xdg-open /tmp/20211-lab-t2-jvarodrigues/assets/boasvindas.html")
