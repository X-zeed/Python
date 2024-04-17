#http://python.nattapon.com/%e0%b9%84%e0%b8%9e%e0%b8%97%e0%b8%ad%e0%b8%99-%e0%b8%8a%e0%b9%88%e0%b8%a7%e0%b8%a2%e0%b9%80%e0%b8%ab%e0%b8%a5%e0%b8%b7%e0%b8%ad%e0%b9%80%e0%b8%81%e0%b8%a9%e0%b8%95%e0%b8%a3%e0%b8%81%e0%b8%a3/
x=int(input())
y=int(input())
a=(x*y)/1600
if (x*y)%1600 > 0:
    a+=1
    
a = int(a)
print(a)
if a*1000>10000:
    print(10000)
else:
    print(a*1000)
