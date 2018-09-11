# http://practice.geeksforgeeks.org/problems/numbers-containing-1-2-and-3/0

t = int(input())

for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    res = []
    for j in range(n):
        num = [int(x) for x in str(a[j])]
        if set(num) <= set([1, 2, 3]) and set(num) & set([1, 2, 3]):
            res.append(''.join([str(x) for x in num]))
    if not res:
        print(-1)
    else:
#        res.sort()
        print(' '.join(list(map(str, res))))
