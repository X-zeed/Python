n=float(input())
s=0
c=0
while n!= -1:
    c+=1
    s+=n
    n=float(input())
if c==0:
    print("No Data")
else:
    print(s/c)