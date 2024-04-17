# print(help(str))
i = 0
for method in dir(str):
    if '__' not in method:
        i += 1
        print(i, method,sep=':')