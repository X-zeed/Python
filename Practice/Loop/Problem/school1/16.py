#Write a Python program that iterates the integers from 1 to 25.
for i in range(0,26):
    if i%4==0 and i%5==0:
        print("fizzbuzz")
    elif i%4==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)