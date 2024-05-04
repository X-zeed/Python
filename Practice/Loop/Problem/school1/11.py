#Python program to count the number of even and odd numbers from a series of numbers.
l=[1,3,5,6,99,134,55]

for i in l:
    if i%2:
        print(f"{i} is an odd number")
    else:
        print(f"{i} is an even number")