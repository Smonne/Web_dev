def f1(a,b,c,x):
   

    if (a < b) and (a < c) and (a < x):

        print (a)

    elif (b < a) and (b < c) and (b < x):

        print (b)

    elif (c < a) and (c < b) and (c < x):

        print (c)

    else:
        print (x)
a , b, c, x = [i for i in str(input()).split()]
f1(a,b,c,x)