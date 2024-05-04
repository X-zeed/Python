#Python program to get the Fibonacci series between 0 to 50.
a=0
b=1
x=0
while x <50:
    x=a+b
    a=b
    b=x
    if x>50:
        break
    print(x)