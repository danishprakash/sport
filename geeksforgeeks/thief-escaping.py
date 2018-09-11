t = int(input())

for i in range(t):
    x, y, n = [int(x) for x in input().split()]
    h = [int(x) for x in input().split()]
    count = 0
    jump = x-y
    for j in range(n):
        temp = h[j]
        while temp > 0:
            if temp <= x:
                temp = 0
                count += 1
                break
            temp -= jump
            count += 1
    print(count)
