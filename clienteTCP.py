import os
from socket import *

nomeServidor = '192.0.2.10'

portaServidor = 12000

socketCliente = socket (AF_INET, SOCK_STREAM)

socketCliente.connect ((nomeServidor, portaServidor))

request = "GET / HTTP/1.1\nHost: boasvindas.ufs \nAccept-Language: pt-br"

socketCliente.send (request.encode())

cabecalho = socketCliente.recv(1024)

print cabecalho

arq = open('/tmp/boasvindas.html', 'w')

dados = cabecalho.split('Content-Type: text/html\n\n')[1]

arq.write(dados)
    
arq.close()

socketCliente.close ()

#os.system('xdg-open /tmp/boasvindas.html')
