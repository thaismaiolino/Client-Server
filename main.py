from threading import Thread
import random
import time
import socket
from sys import argv,exit

filename = 'matriz.txt'

def readFile():
    file = open(filename, 'r')
    preMa1 = file.readline()
    preMa2 = file.readline()
    file.close()

    preMa1 = preMa1[:-2].split(',')
    preMa2 = preMa2[:-1].split(',')

    ma1 = []
    ma2 = []
    for i in range(len(preMa1)):
        item = preMa1[i].split(' ')

        for idx, val in enumerate(preMa1[i].split(' ')):
            aux = int(val)
            item.pop(idx)
            item.insert(idx , aux)

        ma1.append(item)

    for i in range(len(preMa2)):
        item = preMa2[i].split(' ')

        for idx, val in enumerate(preMa2[i].split(' ')):

            aux = int(val)
            item.pop(idx)
            item.insert(idx , aux)

        ma2.append(item)


    return (ma1,ma2)



def sumMatrix(ma1, ma2):
    result = []

    lines = len(ma1)
    cols = len(ma1[0])
    for i in range(lines):
        result.append([])
        for j in range(cols):

            sum = ma1[i][j] + ma2[i][j]
            result[i].append(sum)

    file = open("soma.txt", "w")
    for item in result:
        file.write(str(item))
    file.close()
    print (result)
    return result

def multMatrix(ma1, ma2):
    result = []

    lines = len(ma1)
    cols = len(ma1[0])

    for i in range(lines):
        aux = []
        for j in range(cols):
            mult = 0
            for k in range(len(ma2)):
                mult = mult + ma1[i][k]*ma2[k][j]
            aux.append(mult)
            # aux = str(mult)
        result.append(aux)


    file = open("multiplica.txt", "w")
    for item in result:
        file.write(str(item))
    file.close()

    return result

def generatingMatrix(m):
    file = open(filename, 'w')
    for i in range(m):
        for j in range(m):
            num = random.randint(0, 100)
            file.write(str(num))
            if j < m-1:
                file.write( ' ')
        file.write(',')
    file.write('\n')
    for i in range(m):
        for j in range(m):
            num = random.randint(0, 100)
            file.write(str(num))
            if j < m -1:
                file.write(' ')
        file.write(',')
    file.close()


def executeThreads(file):
    ma1, ma2 = file
    try:
        Thread.start_new_thread( multMatrix(ma1, ma2), ("TH-1", 2, ) )
        Thread.start_new_thread( sumMatrix(ma1, ma2), ("TH-2", 4, ) )
    except:
        print "Error: unable to start thread"




def enviaArquivo(size, connectionType):
    generatingMatrix(size)
    file = readFile()
    print (file)
    connectionType.send(file)
    connectionType.close

def client():
    HOST = '127.0.0.1'     # Endereco IP do Servidor
    PORT = 4040            # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)
    print ('Digite um numero inteiro:')
    num = raw_input()
    enviaArquivo(num, tcp)


def servidor():
    HOST = ''              # Endereco IP do Servidor
    PORT = 4040            # Porta que o Servidor esta

    def conectado(con, cliente):
        print 'Conectado por', cliente

        while True:
            msg = con.recv(1024)
            if not msg: break
            print cliente, msg

        print 'Finalizando conexao do cliente', cliente
        con.close()
        Thread.exit()

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    orig = (HOST, PORT)

    tcp.bind(orig)
    tcp.listen(1)

    while True:
        con, cliente = tcp.accept()
        executeThreads(con)
        con.close()
        Thread.exit()

    tcp.close()

