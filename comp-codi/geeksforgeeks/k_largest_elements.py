t = int(input())
for i in range(t):
    n, k = [int(x) for x in input().split()]
    s = [int(x) for x in input().split()]
    ns = []
    for j in range(k):
        if max(s) not in ns or (max(s) in s and max(s) in ns):
            ns.append(max(s))
            s.remove(max(s))
    print(' '.join([str(x) for x in ns]))
