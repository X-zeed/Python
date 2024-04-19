l=[]
a=input()
c=0

while a!="q":
    l.append(a)
    a=input()
n=len(l)
if n==0:
    print("No Data")
else:
    for i in l:
        c+=float(i)
    print("{:.2f}".format(c/n))