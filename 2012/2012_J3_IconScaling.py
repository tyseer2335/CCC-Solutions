lineOne = "*x*" 
lineTwo = " xx" 
lineThree = "* *" 

k = int(input())
counter = 0

linesArr = [lineOne, lineTwo, lineThree] 

def scaleFactor(line):  
    counter = 0
    newArr = []
    for char in line: 
        while (int(k) > counter): 
            newArr.append(str(char)) 
            counter += 1 
        counter = 0 
    return newArr


for i in range(len(linesArr)): 
    while (int(k) > counter): 
        print(*scaleFactor(linesArr[i]), sep="") 
        counter += 1 
    counter = 0

# 15/15 Solution