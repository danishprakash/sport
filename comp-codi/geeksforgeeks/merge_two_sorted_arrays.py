# http://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays

t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())), reverse=True)
    res = []
    size = n if n > m else m
    a.append(float("inf"))
    b.append(float("inf"))
    p, q = 0, 0
    for j in range((n+m)):
        if p == n:
            [res.append(b[i]) for i in range(q, m)]
            break
        elif q == m:
            [res.append(a[i]) for i in range(p, n)]
            break
        if a[p] > b[q]:
            res.append(a[p])
            p += 1
        else:
            res.append(b[q])
            q += 1
    print(' '.join([str(x) for x in res]))

