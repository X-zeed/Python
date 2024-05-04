n = int(input())
data = input().split()
sum = 0
c=0
for num in data:
    sum += float(num)
average = sum / n
l=input()
print(int(average))
print("%.2f" % average)
for a in l:
    if a in "aeiou":
        l=l.replace(a,'')
        c+=1
print(l,end='')
if c>=3:
    print(' true')
else:
    print(' false')