#Python program that accepts a string and calculates the number of digits and letters.
s=input()
a=0
b=0
for i in s:
    if i.isalpha():
        a+=1
    elif i.isdigit():
        b+=1
print(f"The input string {s} has {a} letters and {b} digits")