import random
n=int(input())
a=random.randint(1,26)
b=random.randint(1,26)
c=random.randint(1,26)
d=random.randint(1,26)
e=random.randint(1,26)
A=(abs(n-a))
B=(abs(n-b))
C=(abs(n-c))
D=(abs(n-d))
E=(abs(n-e))
for i in range(5):
    if A<B and A<C and A<D and A<E:
        print(a)
        break
    elif B<A and B<C and B<D and B<E:
        print(b)
        break
    elif C<A and C<B and C<D and C<E:
        print(c)
        break
    elif D<A and D<B and D<C and D<E:
        print(d)
        break
    elif E<A and E<B and E<C and E<D:
        print(e)
        break
    else:
        print(n)
        break