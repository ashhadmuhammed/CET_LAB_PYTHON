s=input("Enter a string:")
l=len(s)
r=""
for i in range(-1,-l):
    r=r+s[i]
    print(r)    
if(r==s):
    print("string is paliandrome")
else:
    print("not a paliandrome")
    
