# http://practice.geeksforgeeks.org/problems/pairs-with-positive-negative-values/0

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = []
    visited = []
    for j in range(n):
        if a[j]*(-1) in visited:
            res.append(abs(a[j]))
            continue
        visited.append(a[j])
    if not res:
        print(0)
    else:
        res.sort()
        for k in range(len(res)):
            print((str(res[k]*(-1)) + " " + str(res[k]) + " "), end="")
        print()
