# Python program to calculate the sum of all the odd numbers within the given range.
n=int(input())
c=0
for i in range(1,n+1,2):
    c+=i
print(c)