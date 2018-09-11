# http://practice.geeksforgeeks.org/problems/sum-equals-to-sum

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    flag = 0
    for j in range(n):
        for k in range(n):
            if a[j] == a[k]:
                continue
            sum_ = a[j] + a[k]
            if sum_ in d and [k, j] not in d.values():
                print(1)
                flag = 1
                break
            else:
                d[sum_] = [j, k]
            if flag == 1:
                break
    if flag == 0:
        print(0)
