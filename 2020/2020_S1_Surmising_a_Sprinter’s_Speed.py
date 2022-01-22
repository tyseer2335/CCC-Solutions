import math

N = int(input()) 
Observations = [] 
Speeds = [] 

for i in range(N): 
    Time, Position = map(int, input().split())     
    Observations.append((Time, Position))

def SpeedCalc(Data): 
    Index = 1  
    for i in range(len(Data)-1):  
        Speed = (abs(Data[Index-1][1] - Data[Index][1])) / (abs(Data[Index-1][0] - Data[Index][0])) 
        Speeds.append(Speed)  
        Index += 1
    return Speeds
        
Observations.sort() 
print(max(SpeedCalc(Observations)))