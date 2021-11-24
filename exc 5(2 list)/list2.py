s1=0
s2=0
x=[]
b=input("Enter values to the first list")
b=b.split(" ")
b=list(map(int,b))


a=input("Enter values to the first list")
a=a.split(" ")
a=list(map(int,a))
print("First list=",b)
print("Second list=",a)
for i in b:
               s1=s1+i
for i in a:
               s2=s2+i               

if(s1==s2):
               print("sum of two list are equal")

else:
               print("sum is not equal")

print("common values are",end=(''))               
for i in a:
    for j in b:
        if(i==j):
                
            if i not in x:
             print(i," ",end=(''))
             x.append(i)

