n=int(input())
def do(n):
    for a in range(n+1,1,-1):
        for b in range(a+1,1,-1):
            if a+b+((a*a)+(b*b))**0.5==n:
                print("{:.0f}".format(((a*a)+(b*b))**0.5))
                return 0;
do(n)