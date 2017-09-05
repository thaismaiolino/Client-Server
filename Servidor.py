from threading import Thread
import socket
import datetime

filename = 'newmatriz.txt'

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
    # print (result)

    global th2TimeFinish
    th2TimeFinish = datetime.datetime.now()
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

    global th1TimeFinish
    th1TimeFinish = datetime.datetime.now()


    return result


HOST = ''              # Endereco IP do Servidor
PORT = 4040            # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)
newfile = open(filename, 'w')
while True:
    con, cliente = tcp.accept()

    data = con.recv(4096)
    if not data:
            break

    newfile.write(data)
    newfile.close()

    ma1, ma2 = readFile()
    # print ma1, ma2

    global th1TimeStart
    th1TimeStart = datetime.datetime.now()
    print ('TH1 - Tempo inicial:')
    print (str(getattr(th1TimeStart, 'hour'))+'h'+str (getattr(th1TimeStart, 'minute'))+'m'+str(getattr(th1TimeStart, 'second'))+'s'+str(getattr(th1TimeStart, 'microsecond'))+'ms')

    th1 = Thread(target= multMatrix, args=(ma1, ma2) ).start()


    global th2TimeStart
    th2TimeStart = datetime.datetime.now()

    th2 = Thread(target= sumMatrix , args= (ma1, ma2) ).start()

    print ('TH2 - Tempo inicial:')
    print (str(getattr(th2TimeStart, 'hour'))+'h'+str (getattr(th2TimeStart, 'minute'))+'m'+str(getattr(th2TimeStart, 'second'))+'s'+str(getattr(th2TimeStart, 'microsecond'))+'ms')




    readByte = open('multiplica.txt', "rb")
    dataMult = readByte.read()
    readByte.close()

    # print data
    con.send(dataMult)
    con.send('\n')

    readByte = open('soma.txt', "rb")
    dataSoma = readByte.read()
    readByte.close()
    con.send(dataSoma)


    print ('TH1 - Tempo final:')
    print (str(getattr(th1TimeFinish, 'hour'))+'h'+str (getattr(th1TimeFinish, 'minute'))+'m'+str(getattr(th1TimeFinish, 'second'))+'s'+str(getattr(th1TimeFinish, 'microsecond'))+'ms')


    print ('TH2 - Tempo final:')
    print (str(getattr(th2TimeFinish, 'hour'))+'h'+str (getattr(th2TimeFinish, 'minute'))+'m'+str(getattr(th2TimeFinish, 'second'))+'s'+str(getattr(th2TimeFinish, 'microsecond'))+'ms')

    th1total = th1TimeFinish - th1TimeStart
    print ('TH1 - Tempo total:')
    print th1total

    th2total = th2TimeFinish - th2TimeStart
    print ('TH2 - Tempo total:')
    print th2total


con.close()

th1.exit()


th2.exit()

tcp.close()
