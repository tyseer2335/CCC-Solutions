Friends = int(input()) 
Data = [] 

for i in range(Friends): 
    Data.append(input().split())

def SumFinder(Guess): # Function finds the Sum of the walking times
    BooleanArr = []  
    Sum = 0

    for i in Data:  
        if Guess in range(int(i[0])-int(i[2]), int(i[0])+int(i[2])): 
            BooleanArr.append(True) 
        else:   
            BooleanArr.append(False)

    for i in enumerate(Data): 
        if BooleanArr[i[0]] == False: 
            if Guess>int(i[1][0]): 
                Sum += ( Guess - (int(i[1][0]) + int(i[1][2])) ) * (int(i[1][1]))
            elif Guess<int(i[1][0]):  
                Sum += ((int(i[1][0]) - int(i[1][2]) - Guess) * (int(i[1][1])))
    return Sum
    
Low = 0
High = 1000000000 

while (Low<=High): 
    Mid = (Low+High)//2 
    MinSum = SumFinder(Mid)  
    Left = SumFinder(Mid-1)   
    Right = SumFinder(Mid+1)  
    if (MinSum<=Right and MinSum<=Left): 
        break 
    elif (MinSum<Right): 
        High = Mid-1 
    elif (MinSum<Left): 
        Low = Mid + 1
    
print(MinSum)

# CCC 15/15  



    





