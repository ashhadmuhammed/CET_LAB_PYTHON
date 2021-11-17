b=[]
b=input("Enter the sentence")
b=b.split(" ")
n=len(b)
x=[]
c=1
for i in range(0,len(b)):
    for j in range(0,len(b)):
        if(i==j):
               continue;
        if(b[i]==b[j]):
            c+=1
    
    if b[i] not in x: 
     print(b[i],"is repeated ",c,"times")
    x.append(b[i])
    c=1
