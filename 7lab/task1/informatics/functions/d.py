def often(x,y,z):
    cnt_0=0
    cnt_1 =0
    l = [x,y,z]
    for el in l:
        if(el==0):
            cnt_0+=1
        else:
            cnt_1+=1
    if(cnt_0>cnt_1):
        return 0
    return 1
a,b,c = [int(i) for i in str(input()).split()]
print(often(a,b,c))