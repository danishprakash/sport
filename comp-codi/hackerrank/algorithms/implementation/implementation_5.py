n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
counter = 0

for i in range(n):
    for j in range(n):
        if (a[i]+a[j])%k == 0 and i<j:
            counter += 1
print(counter)
