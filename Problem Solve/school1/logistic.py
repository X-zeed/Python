#https://elabsheet.org/elab/taskpads/show/suud9mhj55/
d=int(input())
m=int(input())
t=int(input())
d_f=d+t
if d_f>30:
    m+=1
    d_f-=30
    if m > 12:
        m-=12
print(d_f)
print(m)