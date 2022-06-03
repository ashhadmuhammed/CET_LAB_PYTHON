
d=int(input("date?"))
m=int(input("month"))
count=0
i=0
choc=[2,2,1,3,2]
while((m+i)<=5) :
    sum=sum(choc[i:m+i])
    print(sum)
    if(sum==d):
        count=count+1
    i=i+1

print(count)
         
