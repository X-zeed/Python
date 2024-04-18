text=input()
c=0
a=0
for i in range(0,len(text)):
    if "a" <= text[i] <= "z":
        c=1
    elif 0 <= int(text[i]) <= 9:
        a=1
if c==1 and a==1:
    print("True")
else:
    print("False")