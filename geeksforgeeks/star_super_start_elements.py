# http://practice.geeksforgeeks.org/problems/start-elements/
# Exceeding time limit

t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    mls = []
    max_ = a[0]
    for j in range(n):
        flag = 0
        if a[j] > max_:
            max_ = a[j]
        for k in range(j+1, n):
            if j+1 == n:
                break
            if a[j] <= a[k]:
                flag = 1
        if flag == 0:
            print(a[j], end=' ')
            if a[j] == max_:
                mls.append(a[j])
    print('\n' + ' '.join([str(x) for x in mls]))
