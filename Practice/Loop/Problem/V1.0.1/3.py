text = input()
for i in range(0,10):
    text = text.replace(chr(48+i),"")
print(text)