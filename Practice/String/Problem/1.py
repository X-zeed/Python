text=input()
long  = len(text)
c=1
if long%2==1:
    print("The entered string is not symmetrical")
else:
    for i in range(0, int(long/2)):
        if text[i] != text[i+int(long/2)]:
            c=0
    if c==1:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")
if text == text[::-1]:
    print("The entered string is palindrome")
else:
    print("The entered string is not palindrome")