text=input()
print(text[:int(len(text)/2)],end="")
print(text[int(len(text)/2):].upper())