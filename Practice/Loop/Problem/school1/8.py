#Python program to check if the given string is a palindrome.
s=input()
c=1
for i in range(0,len(s)):
    if s[i]!=s[len(s)-i-1]:
        c=0
        break
if c:
    print("True")
else:
    print("False")