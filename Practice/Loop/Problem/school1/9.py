# Python program that accepts a word from the user and reverses it.
s=input()
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")