
#valida numero de rondas
def validateFirstLine(line):
    try:
        int(line)
        if(int(line) <= 10000):
            return True
        else:
            print("No puede haber mas de 10000 rondas")
            return False
    except:
        print("El dato de ronda debe ser un numero")
        return False
    
#function para crear el archivo con el ganador 
# @params file_name a crear
# @params player1 puntaje max del player1
# @params player2 puntaje maz del player2   
def createOuFile(file_name, player1, player2):
    outStr = ""
    if player1 > player2:
        outStr = "1 " + str(player1)
    else:    
       outStr = "2 " + str(player2)
    
    f = open("./resultados/"+file_name, 'w+', encoding="utf-8")
    f.write(outStr)
    f.close()
    print("Se creo el archivo con el ganador en el directorio resultados")           
 
#funcion para validar que los puntos sean numeros 
def validatePoints(points):
    try:
        int(points[0])
        int(points[1])
        return True
    except:
        print("Los puntos deben ser numeros")
        return False
    
#compara los puntos de ambos jugadores en cada ronda 
def setPointsByPlayer(fm, file_name):

    player1 = 0
    player2 = 0
    validateNum = True

    lines = fm.read().splitlines()

    for line in lines:
        points = line.split(" ")
        if validatePoints(points):#si son numeros
            if int(points[0]) > int(points[1]):#si el puntaje del jugador 1 es mayor
                if player1 < int(points[0]) - int(points[1]):
                    player1 = int(points[0]) - int(points[1])
            else:#si el puntaje del jugador 2 es mayor
                if player2 < int(points[1]) - int(points[0]):
                    player2 = int(points[1]) - int(points[0])
        else:
            validateNum = False
            break

    if(validateNum):
        createOuFile(file_name, player1, player2)                 

 
def openFile(file_name):
    f = open("./marcadores/"+file_name, 'r', encoding="utf-8")
    line = f.readline()
    if validateFirstLine(line):
        setPointsByPlayer(f, file_name)
    f.close()    

def askFileName():
    print("¿Cómo se llama el archivo?")
    file_name = input()
    openFile(file_name)   

askFileName()     