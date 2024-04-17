c=0
for i in range(0,5):
    for j in range(i,5):
        print(" ",end="")
    for j in range(0,i+1):
        print(chr(65 + c),"",end="")
        c+=1
    print()