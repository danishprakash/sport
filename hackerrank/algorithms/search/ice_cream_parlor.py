# https://www.hackerrank.com/challenges/icecream-parlor

t = int(input())

for i in range(t):
    m = int(input())
    n = int(input())
    c = [int(x) for x in input().split()]
    flag = 0
    for j in range(len(c)):
        for k in range(len(c)):
            if j == k:
                continue
            if c[j]+c[k] == m:
                flag = 1
                print(str(j+1), str(k+1))
                break
        if flag == 1:
            break
