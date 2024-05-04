s=0
for i in range(4):
   n=int(input())
   if 100000<=n<=500000:
       s+=n*0.05
   elif 500001<n<=1000000:
       s+=n*0.1
   elif n>=1000001:
       s+=n*0.2
print('%.2f' % s)