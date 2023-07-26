
def validateFirstLine(line):
    try:
        int(line)
        return True
    except:
        print("El numero de ronda debe ser un numero")
        return False

def countPoints(fm):

    player1 = []
    player2 = []

    lines = fm.read().splitlines()

    for line in lines:
        points = line.split(" ")
        player1.append(points[0])
        player2.append(points[1])
    print(player1)
    print(player2)    


def openFile(file_name):
    f = open("./marcadores/"+file_name, 'r', encoding="utf-8")
    line = f.readline()
    if validateFirstLine(line):
        countPoints(f)
    f.close()    


openFile("juego1")    