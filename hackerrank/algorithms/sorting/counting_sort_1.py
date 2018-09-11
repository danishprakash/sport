n = int(input())
a = [int(x) for x in input().split()]
b = [0 for x in range(len(a))]
c = [0 for x in range(max(a)+1)]
print(a)
print(b)
for i in range(len(a)):
    c[a[i]] += 1
    print(c)
for j in range(1, len(c)):
    c[j] += c[j-1]
for k in range(len(a)-1,0, -1):
    print(k)
    b[c[a[k]]] = a[k]
    c[a[k]] -= 1
print(b)
