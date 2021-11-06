word = str(input()) 

letters = ["I", "O", "S", "H", "Z", "X", "N"]
arr = []

for i in range(len(word)): 
    for j in letters: 
        if (word[i] == j):   
            arr.append(j)  

finalWord = "".join(arr)  

if (word == str(finalWord)): 
    print("YES") 
else: 
    print("NO") 

# 15/15 CCC



    