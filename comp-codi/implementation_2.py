s, t = [int(s) for s in input().split()]
a, b = [int(s) for s in input().split()]
m, n = [int(s) for s in input().split()]
apples = [int(s) for s in input().split()]
oranges = [int(s) for s in input().split()]

appleCounter = 0
orangeCounter = 0

for i in range(m):
    if (apples[i] + a) in range(s, t+1):
        appleCounter += 1

for i in range(n):
    if (oranges[i] + b) in range(s, t+1):
        orangeCounter += 1

print(appleCounter)
print(orangeCounter)
