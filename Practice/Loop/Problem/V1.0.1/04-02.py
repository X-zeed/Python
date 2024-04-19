d = [int(e) for e in input().split()] 

n=len(d)
p=d[n-1]
i=-1
j=0

while j<n-1:
    if d[j]<=p:
        i+=1
        t=d[i]
        d[i]=d[j]
        d[j]=t
    j+=1

t=d[n-1]
d[n-1]=d[i+1]
d[i+1]=t
print(d)