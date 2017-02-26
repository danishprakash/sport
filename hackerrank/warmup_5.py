n = int(input())

lst = []
for i in range(n):
    lst.append([int(x) for x in input().split()])
ldiag = 0

for i in range(len(lst)):
    for j in range(len(lst[0])):
        if i == j:
            ldiag += lst[i][j]


print(ldiag)
#print(lst)
