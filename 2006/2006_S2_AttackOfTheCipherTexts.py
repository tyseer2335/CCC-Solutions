english = input() 
cipher1 = input()  
cipher2 = input()  

# english = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG" 
# cipher1 = "UIFARVJDLACSPXOAGPYAKVNQTAPWFSAUIFAMB ZAEPH"
# cipher2 = "XFABSFAWFSZACBEAQFPQMFAEPJOHAWFSZACBEAUIJOHTAIBAIB"

text = { 
    "A":"", 
    "B":"",  
    "C":"", 
    "D":"", 
    "E":"", 
    "F":"", 
    "G":"", 
    "H":"", 
    "I":"",
    "K":"", 
    "L":"", 
    "M":"", 
    "N":"", 
    "O":"", 
    "P":"", 
    "Q":"", 
    "R":"", 
    "S":"", 
    "T":"", 
    "U":"", 
    "V":"", 
    "W":"", 
    "X":"", 
    "Y":"", 
    "Z":""
}  

for i in range(len(english)): 
    text[english[i]] = cipher1[i] 

text = dict((i,j) for j,i in text.items())

for i in cipher2:  
    try:
        print(text[i], end="") 
    except KeyError: 
        print(".", end="")