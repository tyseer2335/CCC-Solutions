count = 0
arr = [] 
arr2 = [] 
arr3 = []

while  (count<4): 
    n =   list(map(int, input().split()))
    count +=1 
    arr.append(n) 

for i in arr: 
     sum = 0 
     for j in i: 
         sum += j   
     arr2.append(int(sum))   
 
counter2 = 0
while (counter2 != 4): 
    nextSum = 0 
    for i in range(len(arr)):   
        nextSum += arr[i][counter2]  
    counter2 += 1 
    arr3.append(int(nextSum))

if len(set(arr2))>1 or len(set(arr3))>1: 
    print("not magic") 
else: 
    print("magic") 


# CCC 15/15


