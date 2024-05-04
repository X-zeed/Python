text=input()
text=text.split()
l=[]
for i in text:
    long=len(i)
    for j in range(0,len(i)):
        if j==0 :
            l.append(i[0].upper())
        elif j==len(i)-1:
            l.append(i[-1].upper())
            l.append(" ")
            c=0
        else:
            l.append(i[j])

print("".join(l))
# print(l)