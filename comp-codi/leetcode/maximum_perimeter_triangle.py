# https://www.hackerrank.com/challenges/maximum-perimeter-triangle/

n = int(input())
a = [int(x) for x in input().split()]
max_ = 0
ls = []

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if i == j or j == k or i == k:
                continue
            if (a[i] + a[j] > a[k]) and (a[i] + a[k] > a[j]) and (a[j] + a[k] > a[i]) and (sum([a[i], a[j], a[k]]) > max_):
                if sorted([a[i], a[j], a[k]]) not in ls:
                    ls.append(sorted([a[i], a[j], a[k]]))
                max_ = sum([a[i], a[j], a[k]])

max_ = 0
min_ = 0
flag = -1
ml = []
for i in range(len(ls)):
    if max(ls[i]) >= max_:
        max_ = max(ls[i])
        ml.append(ls[i])
        flag = i
if len(ml) > 1:
    for i in range(len(ml)):
        if min(ls[i]) < min_:
            flag = i

if flag == -1:
    print(-1)
else:
    ls = ls[flag]
    print(' '.join([str(x) for x in ls]))
