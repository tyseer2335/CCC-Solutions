n = int(input()) 

A = 100 
D = 100

rolls = []

for i in range(0,n): 
    x = input() 
    rolls.append(x)
    
for i in rolls: 
    if ( int(i[0]) < int(i[2])):
        A -= int(i[2])  
    elif ( int(i[0]) > int(i[2])):  
        D -= int(i[0])   


print(A)
print(D)

# CCC 15/15 Solution