text1=input()
text2=input()
l=[]

for i in range(0,len(text1)-1):
    for j in range(0,i):
        if text1[i] == text1[j]:
            c = text1[i] 
            text1 = text1.replace(text1[i]," ");
            text1 = text1 + c;
for i in range(0,len(text2)-1):
    for j in range(0,i):
        if text2[i] == text2[j]:
            c = text2[i] 
            text2 = text2.replace(text2[i]," ");
            text2 = text2 + c;
            
for i in range(0, len(text1)):
    for j in range(0, len(text2)):
        if text1[i] != " " and text1[i] == text2[j]:
            l.append(text1[i])
            text1[i].replace(text1[i],"")
            text2[j].replace(text2[j],"")

s = "".join(l)
long = len(s)
st = ", ".join(l)
print(long)
print("(i.e. matching characters : - " + st + ")")