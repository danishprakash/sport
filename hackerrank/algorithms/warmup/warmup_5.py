n = int(input())

lst = []
for i in range(n):
    lst.append([int(x) for x in input().split()])

ldiag = 0
rdiag = 0

for i in range(len(lst)):
    for j in range(len(lst[0])):
        if i == j:
            ldiag += lst[i][j]
        if (i+j) == n-1:
            rdiag += lst[i][j]
abSum = abs(ldiag-rdiag)

print(abSum)
#print(lst)
