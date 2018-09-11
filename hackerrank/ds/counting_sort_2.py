n = int(input())
a = [int(x) for x in input().split()]
b = a
c = [0 for x in range(max(a)+1)]
for i in range(len(c)):
    c[i] = 0

for i in range(len(a)):
    c[a[i]] += 1

print(c)
for i in range(1, len(c)):
    c[i] += c[i-1]

for i in range(len(a)):
    b[c[a[i]]] = a[i]
    c[a[i]] -= 1

print(' '.join([str(x) for x in b]))
