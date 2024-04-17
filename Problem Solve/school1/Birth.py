#http://python.nattapon.com/%e0%b9%84%e0%b8%9e%e0%b8%97%e0%b8%ad%e0%b8%99-%e0%b8%ad%e0%b8%b2%e0%b8%a2%e0%b8%b8%e0%b9%80%e0%b8%97%e0%b9%88%e0%b8%b2%e0%b9%84%e0%b8%ab%e0%b8%a3%e0%b9%88%e0%b8%81%e0%b8%b1%e0%b8%99%e0%b8%99%e0%b8%b0/
m1 = int(input())
y1 = int(input())
m2 = int(input())
y2 = int(input())
y = y2 - y1
m = m2 - m1
if(m<0):
  y = y - 1
  m = 12 + m
print(y)
print(m)