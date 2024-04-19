#Python program to display all numbers within a range except the prime numbers.
import math
for i in range(10,30):
    if i<0:
        continue    
    for j in range(2,int(math.sqrt(i))+1):
        if not i % j:
            print(i)
        else:
            continue
        break