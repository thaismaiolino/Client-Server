import random
import socket

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

def enviaArquivo(size):

    generatingMatrix(size)
    file = readFile()
    print file
    return str(file)

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



HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 4040            # Porta que o Servidor esta

print ('Digite um numero inteiro:')
num = raw_input()
num = int(num)
generatingMatrix(num)
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print readFile()
while True:

    readByte = open(filename, "rb")
    data = readByte.read()
    readByte.close()

    tcp.send(data)

    dataRecv = tcp.recv(500)
    print dataRecv
    if not dataRecv:
        break

tcp.close