n = int(input())
p = int(input())

if p == 1 or p == n:
    print(0)
elif p == n-1 and n%2 == 0:
    print(1)
elif n-p <= p-1:
    print((n-p)//2)
elif p %2 != 0:
    print((p-1-1)//2+1)
else:
    print((p-1)//2+1)

