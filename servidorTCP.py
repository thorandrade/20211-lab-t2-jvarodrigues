from socket import *

portaServidor = 12000

socketServidor = socket (AF_INET, SOCK_STREAM)

socketServidor.bind (('', portaServidor))

socketServidor.listen (1)

print "O servidor esta pronto para receber solicitacoes"

while 1 :

    socketConexao, endereco = socketServidor.accept ()

    request = socketConexao.recv (1024)

    print request
    
    if request.find("DEC") == 11:
        if request.find("AQ") == 23:
            print "entrei aqui"
            arq = open('/tmp/20211-lab-t2-jvarodrigues/assets/boasvindasAQ.html', 'r')
            for i in arq.readlines():
                socketConexao.send(i)
            arq.close()
        if request.find("EC") == 23:
            arq = open('/tmp/20211-lab-t2-jvarodrigues/assets/boasvindasEC.html', 'r')
            for i in arq.readlines():
                socketConexao.send(i)
            arq.close()
    elif request.find("1.1") == 11:
        arq = open('/tmp/20211-lab-t2-jvarodrigues/assets/boasvindasUFS.html', 'r')
        for i in arq.readlines():
            socketConexao.send(i)
        arq.close()
    socketConexao.close ()