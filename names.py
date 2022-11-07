import numpy
import math
def names(namesRequired):
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numCol = math.ceil((math.log(namesRequired)/math.log(26)))
    numRows = (len(letters)**numCol)
    names = numpy.empty((numRows, numCol),dtype=str)

    currentLet = 0
    divisor = 1
    nameCount = 0
    for currentCol in range(1,numCol+1):
        for tableIndex in range(1, numRows+1):
            names[tableIndex-1,currentCol-1] = letters[currentLet]
            if tableIndex % divisor == 0:
                currentLet += 1
                if currentLet > len(letters)-1:
                    currentLet = 0

        divisor = divisor * len(letters)
    return names
