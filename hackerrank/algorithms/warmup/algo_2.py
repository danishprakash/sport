a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

aScore = 0
bScore = 0

for i in range(len(a)):
    if a[i] > b[i]:
        aScore += 1
    elif b[i] > a[i]:
        bScore += 1

print(aScore, bScore)
