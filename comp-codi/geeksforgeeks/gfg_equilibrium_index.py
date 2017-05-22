def findEquilibrium(n, a):
    sumleft = 0
    sumright = 0
    for i in range(0, n):
        for j in range(0,i):
            sumleft += a[j]
        for k in range(i+1,n):
            sumright += a[k]
        if sumleft == sumright:
            print(i)
            break
        else:
            if i+1 == n:
                print('-1')
                break
            sumleft, sumright = [0,0]

n = int(input())
a = [int(s) for s in input().split()]

findEquilibrium(n, a)
