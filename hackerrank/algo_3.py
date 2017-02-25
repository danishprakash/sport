n = int(input())
a = [int(x) for x in input().split()]

aSum = 0

for i in range(n):
    aSum += a[i]

print(aSum)
