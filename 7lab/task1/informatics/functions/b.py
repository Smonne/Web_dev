def power_n(a, n):
    res=1
    for i in range(int(n)):
        res*=a
    return int(res)
b,c = [i for i in str(input()).split()]
b= float(b)
c= float(c)
print(power_n(b,c))