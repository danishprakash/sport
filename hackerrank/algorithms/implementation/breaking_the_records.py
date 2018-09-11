n = int(input())
s = [int(x) for x in input().split()]

min_score, max_score = [s[0], s[0]]
min_count, max_count = [0, 0]

for i in range(1, n):
    if s[i] > max_score:
        max_score = s[i]
        max_count += 1
    elif s[i] < min_score:
        min_score = s[i]
        min_count += 1

print(max_count, min_count)
