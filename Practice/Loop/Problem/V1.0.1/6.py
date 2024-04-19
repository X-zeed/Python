text=input()
text=text.split()
l=[]
for i in text:
    if not len(i)%2:
        l.append(i)
print(" ".join(l))