# import math

# N = int(input())  
# h = input()  
# w = input()  
# heights = []
# widths = []


# for i in h:  
#     if (i != " "):
#         heights.append(i) 

# for i in w:  
#     if (i != " "):
#         widths.append(i)


# p1 = 0 
# p2 = 1 
# A = 0

# for i in range(N): 
#     # print(heights[p1], heights[p2], widths[i])  
#     a = (int(widths[i])) * ((int(heights[p1]) + int(heights[p2])))/2 
#     A += a 
#     p1 += 1 
#     p2 += 1 

# print(A)

numFence = int(input()) 
height = input().split() 
width = input().split() 

area = 0
for i in range(numFence): 
    area += (int(width[i])) * ((int(height[i]) + int(height[i+1])))/2 

print(area)