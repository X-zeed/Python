#A=65
c=65
for i in range(0,5):
    for j in range(0,i+1):
        print(chr(c)," ",end="")
        c+=1
    print()