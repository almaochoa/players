
def validateFirstLine(line):
    try:
        int(line)
        return True
    except:
        print("El numero de ronda debe ser un numero")
        return False
    
def createOuFile(player1, player2):
    outStr = ""
    if player1 > player2:
        outStr = "1 " + str(player1)
    else:    
       outStr = "2 " + str(player2)

    print(outStr)   
 
def setPointsByPlayer(fm):

    player1 = 0
    player2 = 0

    lines = fm.read().splitlines()

    for line in lines:
        points = line.split(" ")
        print(points)
        if int(points[0]) > int(points[1]):
            if player1 < int(points[0]) - int(points[1]):
                player1 = int(points[0]) - int(points[1])
        else:
            if player2 < int(points[1]) - int(points[0]):
                player2 = int(points[1]) - int(points[0])

    createOuFile(player1, player2)                 

def openFile(file_name):
    f = open("./marcadores/"+file_name, 'r', encoding="utf-8")
    line = f.readline()
    if validateFirstLine(line):
        setPointsByPlayer(f)
    f.close()    


openFile("juego1")    