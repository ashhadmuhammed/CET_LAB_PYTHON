n=int(input("Enter the limit:"))
a=0
b=1
s=0
count=1
while(count<=n):
    print(s,end=(" "))
    a=b
    b=s
    s=a+b
    count+=1
   
