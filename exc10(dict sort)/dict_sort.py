d={1:1000,2:500,3:55,4:56,5:301}
a=[]
print("Before sorting:",d)
a=sorted(d.items(),key=lambda x:x[1])
print("After sorting sorting:",a)
