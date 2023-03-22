x= (int(input()))
def is_valid(n):
    
        if(((n[0]==str(4)) or(n[0]==str(5))) or(n[0]==str(6))):
            
            if((len(n)==19)and (n[4]=='-' and n[9]=='-' and n[14]=='-')):
                n = n.replace('-', '')
            if(len(n)==16):
                    
                    d={}
                    for el in n:
                        if el in d.keys():
                            d[el]+=1
                        else:
                            d[el]=1
                

                    for v in d.values():
                        #return True
                        if (v>4):
                            return False
                    
                    for el in n:
                            if (el.isdigit()==False):
                                return False
                    return True
        return False
for i in range(x):
        n = str(input())
        print('Valid' if (is_valid(n)==True) else 'Invalid')

