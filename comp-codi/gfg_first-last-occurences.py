import sys

t = int(input())

for item in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    x = int(input())
    first = last = flag = 0
    for i in range(n):
        if x not in a:
            flag = 1
            break
        if a[i] == x and first == 0:
            first = i
            last = i
        elif a[i] == x and last > 0:
            last = i
        # print(last)
    if flag == 0:
        print(first, last)
    else:
        print('-1')
