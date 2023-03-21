n = int(input()) 
a = [int(i) for i in input().split()]
p=0
for i in a :
    if(i>0):
        p+=1
print(p)