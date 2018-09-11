# http://practice.geeksforgeeks.org/problems/chocolate-station/

t = int(input())

for k in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    p = int(input())
    cost = 0
    count = 0
    if a[0] > 0:
        cost += a[0]*p
    for i in range(n-1):
        print(count, cost, a[i], a[i+1])
        if a[i] - a[i+1] >= 0:
            count += a[i] - a[i+1]
        else:
            if a[i] - a[i+1] < count:
#                cost += (count+(a[i]-a[i+1]))*p
                count -= abs(a[i]-a[i+1])
        if count < 0:
            cost += abs(count)*p
            count = 0
    print(cost)
            
