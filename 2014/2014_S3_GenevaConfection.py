T = int(input())

Cars = [[] for i in range(T)] 

ListOne = [] 
ListTwo = []

def Length(list):
    count = 0
    for i in list:
        count += 1
    return count

for i in range(0,T): 
    N = int(input()) 
    
    while (Length(Cars[i])<N): 
        x = int(input())
        Cars[i].insert(0,x) 


for i in Cars:  
    y = 1 
    arr = [] 

    for j in i:  
        if (not j == y):  
            arr.insert(0,j)
        else:   
            y += 1
    ListOne.append(arr)
    ListTwo.append(y)  

for i in range(len(ListOne)): 
        if (ListOne[i][0] == ListTwo[i]): 
            print("Y") 
        else: 
            print("N") 
        

# 3/15 CCC