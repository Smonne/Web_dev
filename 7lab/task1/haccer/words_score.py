n = int(input())
l = [i for i in str(input()).split()]
vowels = ['e', 'u', 'i', 'o', 'a', 'y','E', 'U', 'I', 'O','A','Y']
sum = 0
for el in l:
    cnt = 0
    for letter in el:
        if(letter in vowels):
            cnt+=1
    if(cnt%2==0):
        sum+=2
    else:
        sum+=1
    #print('current_sum '+ str(sum))
print(sum)
