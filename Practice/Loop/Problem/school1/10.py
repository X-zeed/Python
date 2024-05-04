n=int(input())
s=str(n)
l=len(s)
c=0
for i in s:
    c+=int(i)**l
if c == n:
    print("Amstrong number")
else:
    print("Not Amstrong number")