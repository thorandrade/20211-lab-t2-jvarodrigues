from socket import *

portaServidor = 12000

ipServidor = '192.0.2.10'

socketServidor = socket (AF_INET, SOCK_STREAM)

socketServidor.bind ((ipServidor, portaServidor))

socketServidor.listen (1)

print 'O servidor esta pronto para receber solicitacoes'

while 1 :

    socketConexao, endereco = socketServidor.accept ()

    request = socketConexao.recv (1024)

    print request
    
    if request.find('DEC') == 11:
        if request.find('AQ') == 23:
            cabecalho = 'HTTP/DEC OK\nContent-Type: text/html\n\n'
            socketConexao.send (cabecalho.encode())
            arq = open('/tmp/20211-lab-t2-jvarodrigues/assets/boasvindasAQ.html', 'r')
            for i in arq.readlines():
                socketConexao.send(i)
            arq.close()
        elif request.find('EC') == 23:
            print 'entrei aqui'
            cabecalho = 'HTTP/DEC OK\nContent-Type: text/html\n\n'
            socketConexao.send (cabecalho.encode())
            arq = open('/tmp/20211-lab-t2-jvarodrigues/assets/boasvindasEC.html', 'r')
            for i in arq.readlines():
                socketConexao.send(i)
            arq.close()
    elif request.find('1.1') == 11:
        cabecalho = 'HTTP/1.1 OK\nContent-Type: text/html\n\n'
        socketConexao.send (cabecalho.encode())
        arq = open('/tmp/20211-lab-t2-jvarodrigues/assets/boasvindasUFS.html', 'r')
        for i in arq.readlines():
            socketConexao.send(i)
        arq.close()
    socketConexao.close ()