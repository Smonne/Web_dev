n = int(input()) 
a = [int(i) for i in input().split()]
p=0
for i in range(1,len(a)):
    if((a[i]>0 and a[i-1]<0)or (a[i]<0 and a[i-1]>0)):
        p+=1
if(p!=n):
    print("YES")
else:
    print("NO")