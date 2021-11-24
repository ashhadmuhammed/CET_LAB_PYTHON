num=int(input("Enter a Number:"))
l=(num//2)+1
c=0
for i in range(2,l):
        if(num%i==0):
            c=1
            break;
if(c==0):
        print(num," is Prime")

else:
        print(num,"is not a prime")

    
        
        
        
