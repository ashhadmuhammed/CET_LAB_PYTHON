a=input("Enter string1:")
b=input("Enter string2:")
print("Before swapping")
print(a,"  ",b)
c=b
b=a[0:2]+b[2:]
a=c[0:2]+a[2:]
print("After swapping\n",a+" "+b)
