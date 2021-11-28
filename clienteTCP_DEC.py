import os
import webbrowser
from socket import *

nomeServidor = '192.0.2.10'

portaServidor = 12000

socketCliente = socket (AF_INET, SOCK_STREAM)

socketCliente.connect ((nomeServidor, portaServidor))

curso = raw_input ('Informe o codigo do seu curso\n   AQ - Arquitetura\n   EC - Engenharia Civil\nQual o seu curso: ')

request = "GET / HTTP/DEC \nCurso: " + curso + "\nHost: boasvindas.ufs \nAccept-Language: pt-br"

socketCliente.send (request.encode())

print "Recebendo pagina de boas vindas"

arq = open('/tmp/boasvindas.html', 'w')

while 1:
    dados = socketCliente.recv(1024)
    if not dados:
        break
    arq.write(dados)
    
arq.close()

socketCliente.close ()

webbrowser.open("http://www.google.com")

#os.system('xdg-open /tmp/boasvindas.html')
