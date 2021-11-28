a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

def gcd(c,d):
    if(c>d):
        small=d
    else:
         small=c
    for i in range(small+1,1,-1):
        if(c%i==0 and d%i==0):
            gcdn=i
            break;
    return(gcdn)
             
a=gcd(a,b)
print(a)
