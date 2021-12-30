M = int(input()) # col
N = int(input()) # row
K = int(input()) 
Choices = []

Canvas = [[False for i in range (N)] for j in range(M)] 

for i in range(K): 
    Choices.append(input().split())

def invertBool(b):  
    if b == True: 
        b = False 
    else: 
        b = True
    return(b)
    
def Painter(ChoiceArr):   
    for i in ChoiceArr: 
        if i[0] == "R":    
            for j in range(N):  
               Canvas[int(i[1])-1][j] = invertBool(Canvas[int(i[1])-1][j])    
        elif i[0] == "C":
            for j in range(M):  
               Canvas[j][int(i[1])-1] = invertBool(Canvas[j][int(i[1])-1]) 

Painter(Choices) 

count = 0
for i in Canvas: 
    for j in i: 
        if j == True: 
            count += 1

print(count)





