AR = input() 
sum = 0

arr = [x for x in AR] 

for i, v in enumerate(arr): 
    if (v == "I"): 
        arr[i] = 1
    elif (v == "V"): 
        arr[i] = 5   
    elif (v == "X"): 
        arr[i] = 10  
    elif (v == "L"): 
        arr[i] = 50 
    elif (v == "C"): 
        arr[i] = 100  
    elif (v == "D"): 
        arr[i] = 500  
    elif (v == "M"): 
        arr[i] = 1000 

arr = [ int(x) for x in arr]
arr2 = [[] for x in range(int(len(arr)/2))] 

counter1 = 0
counter2 = 1
for i in range(len(arr2)):  
    
    while(len(arr2[i])<2): 
        arr2[i].append(arr[counter1])  
        counter1 += 2
        arr2[i].append(arr[counter2]) 
        counter2 += 2
       
for i in range(0,len(arr2)): 
    try:
        if (arr2[i][1] < arr2[i+1][1]): 
            arr2[i][0] = (arr2[i][0])*(-1)   
    except IndexError: 
        break

for i,v in enumerate(arr2):  
    product = v[0]*v[1]  
    sum += product

print(sum) 

# 15/15 CCC