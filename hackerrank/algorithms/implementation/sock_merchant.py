n = int(input())
s = [int(x) for x in input().split()]
dc = {}
count = 0

for i in range(n):
    if s[i] not in dc:
        dc[s[i]] = 1
    else:
        del dc[s[i]]
        count += 1

print(count)
