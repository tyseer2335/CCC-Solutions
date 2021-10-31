a = int(input()) 
b = int(input())

# a = 1
# b = 1000

coolCounter = 0

def isPerfectSquare (num): 
    root = num**(1/2)  
    if int(root + 0.5) ** 2 == num:  
        return True 

def isPerfectCube (num): 
    cubeRoot = num**(1/3) 
    if int(cubeRoot + 0.5) ** 3 == num: 
        return True 


# cubes = [i for i in range(a, b+1) if isPerfectCube(i)] 

cubes = [0] 

# for i in range (a, b+1): 
#     if (b>i**3): 
#         cubes.append(i**3)


j = 1
while (b>cubes[-1]):  
    cubes.append(j**3) 
    j += 1

del cubes[0]

if (b<cubes[-1]): 
    del cubes[-1]


cubesTwo = []

for i in range(len(cubes)): 
    if (a<=cubes[i]):  
        cubesTwo.append(cubes[i])


for i in cubesTwo: 
    if (isPerfectSquare(i)): 
        coolCounter += 1  
print(coolCounter) 
    

# 15/15 Solution CCC

