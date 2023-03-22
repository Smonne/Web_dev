def is_leap(year):
    leap = False
    
    # Write your logic here
    leap = True if((year%4==0 and year%100!=0)or (year%400==0)) else False
    
    return leap

year = int(input())