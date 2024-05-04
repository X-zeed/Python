w=float(input())
h=float(input())
c=0
while w>0 and h>0:
    height=h/100
    if (w/(height*height)<18.5):
        c+=1
    w=float(input())
    h=float(input())
print(c)