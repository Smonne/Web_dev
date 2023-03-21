import math
a, b = int(input()),int(input())
for i in range(a,b+1):
    c= int(math.sqrt(i))
    if(c*c==i):
        print(i, end=" ")