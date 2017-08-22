# https://www.hackerrank.com/contests/gs-codesprint/challenges/trader-profit

q = int(input())
for i in range(q):
    k = int(input())
    n = int(input())
    t = [int(x) for x in input().split()]
    gmax = []
    count = 0
    prev = t[0]
    i = 1

    while i < n:
        nmax = []
        flag = 0
        if t[i] < prev:
            prev = t[i]
            continue
        else:
            print('inside else')
            for j in range(i, n):
                if t[j] < prev:
                    prev = t[j]
                    i = j+1
                    flag = 1
                    break
                else:
                    nmax.append(t[j] - prev)
                    i = j
        print(prev, t[i], nmax, i)
        gmax.append(max(nmax))
        if flag == 0:
            i += 1
    
    print(gmax)
