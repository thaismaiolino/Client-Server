from threading import Thread

filename = 'matriz.txt'
# LER O FILE
# VERIFICAR SE TEM 2 MATRIZES DENTRO DELE
# RECEBER ESSAS 2 MATRIZES DO CHECKMATRIZ
def readFile():
    file = open(filename, 'r')
    checkMatriz(file)
    # print(file.read())

# CHECAR SE TEM 2 MATRIZES E USAR O METODO DE ISQUARE PRA VER SE NAO QUADRATICAS
def checkMatriz(file):
    col = file.readline()
    file.closed

    num = len(col.split(' '))
    matriz = []

    for col in file.read():
        print col
        if not col.startswith('\n'):
            matriz.append(col)
        else:
            matriz = []

    print (matriz)

def isSquare (matrix):
    return all (len (row) == len (matrix) for row in matrix)


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
    file.write(result)
    file.close()
    return result

def multMatrix(ma1, ma2):
    result = []

    lines = len(ma1)
    cols = len(ma1[0])

    for i in range(lines):
        result.append([])
        for j in range(cols):
            mult = 0
            for k in range(len(ma2)):
                mult = mult + ma1[i][k]*ma2[k][j]
            result.append(mult)


    file = open("multiplica.txt", "w")
    file.write(result)
    file.close()
    return result

def executeThreads(ma1,ma2):
    try:
        Thread.start_new_thread( multMatrix(ma1, ma2), ("TH-1", 2, ) )
        Thread.start_new_thread( sumMatrix(ma1, ma2), ("TH-2", 4, ) )
    except:
        print "Error: unable to start thread"


