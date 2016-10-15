from threading import Thread
import random

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
    ma1 = []
    ma2 = []
    for i in range(m):
        auxMa1 = []
        auxMa2 = []
        for j in range(m):

            numMa1 = random.randint(0, 100)
            numMa2 = random.randint(0, 100)
            auxMa1.append(numMa1)
            auxMa2.append(numMa2)

        ma1.append(auxMa1)
        ma2.append( auxMa2)

    return ma1, ma2

def generatingMatrix2(m):
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



def writeMatrix(m):
    matrix = generatingMatrix(m)
    file = open(filename, 'w')
    for item in matrix:
        file.write(str(item))
    file.close()


def executeThreads(ma1,ma2):
    try:
        Thread.start_new_thread( multMatrix(ma1, ma2), ("TH-1", 2, ) )
        Thread.start_new_thread( sumMatrix(ma1, ma2), ("TH-2", 4, ) )
    except:
        print "Error: unable to start thread"


# writeMatrix(4)
# generatingMatrix2(3)
ma1, ma2 = readFile()


sumMatrix(ma1, ma2)

