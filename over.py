a=input("Enter the numbers").split(" ")
a=list(map(int,a))
for i in range(0,len(a)):
    if a[i]>100:
        a[i]='over'
    
print(a)
