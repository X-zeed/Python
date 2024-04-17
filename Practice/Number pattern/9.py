n=int(input())
n+=1
# for i in range(1,n):
#     for j in range(i,n):
#         print(j," ",end="")
#     print()

for i in range(1,n):
    for j in range(1,i):
        print(i," ",end="")
    for j in range(i,n):
        print(j," ",end="")
    print()