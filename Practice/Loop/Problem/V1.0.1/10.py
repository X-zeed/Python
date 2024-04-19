text=input().lower()
case="aeiou"
l=[]
for i in range(0,len(text)):
    if text[i] in case:
        case=case.replace(text[i],"")
if not len(case):
    print("All vowels are present")
else:
    for i in range(len(case)):
        l.append("'"+case[i]+"'")
    print("All vowels except " + " , ".join(l) + " are not present")