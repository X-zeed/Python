n=int(input())
c=0
for i in range(n):
    if not i%3 or not i%5:
        c+=i
print(c)