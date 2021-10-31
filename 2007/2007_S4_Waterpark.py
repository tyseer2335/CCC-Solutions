n = int(input()) 
paths = 0 
points = []
p = ""

tempArr = []

while (p != "0 0"):
    arr = []
    p = input() 
    arr.append(p) 
    points.append(arr)

del points[-1]

for i in range(len(points)):  
    
    if (points[i][0][0] == "1" and points[i][0][2] == str(n)):  
        del points[i]
        paths += 1   
        break
    


increment = 2
for i in range(len(points)): 
  try :  
      tempArr.append(points[i])   
      if (points[i][0][-1] == points[i+1][0][0]):  
          tempArr.append(points[i+1]) 
      elif (points[i][0][-1] == points[i+ increment][0][0]): 
        #   tempArr.append(points[i])  
          tempArr.append(points[i + increment]) 
    #   elif (points[i + increment][0][0] == str(n)):  
    #       increment = 0  
      elif (points[i][0][-1] != points[i+ increment][0][0]): 
          increment += 1  
      

  except IndexError: 
    break
  


for i in range(len(tempArr)):   
  try: 
    if (tempArr[i][0][-1] == str(n)): 
     paths += 1 

     del tempArr[i] 
     del points[i]

  except IndexError: 
    break
     


print(tempArr) 
print(points) 
print(paths) 


# CCC 0/15