
def validateFirstLine(line):
    try:
        int(line)
        return True
    except:
        print("El numero de ronda debe ser un numero")
        return False

def countPoints(fm):
    for line in fm:
        print(line, end='')
        #num_line = num_line+1


def openFile(file_name):
    f = open("./marcadores/"+file_name, 'r', encoding="utf-8")
    line = f.readline()
    if validateFirstLine(line):
        countPoints(f.read())
    f.close()    

    """
    for line in f:
        if num_line == 0:
            first_valid = validateFirstLine(line)
        else:
            if first_valid:                        
                print(line, end='')
                countPoints()
        num_line = num_line+1
    """    

openFile("juego1")    