def logic_or(b,c ):
    if(b==c):
        if(b==1 or b==0):
            return 0
    return 1
b,c = [int(i) for i in str(input()).split()]

print(logic_or(b,c))