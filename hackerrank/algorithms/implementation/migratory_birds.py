n = int(input())
b = [int(x) for x in input().split()]
max_count = [0 for x in range(6)]
for i in range(n):
    max_count[b[i]] += 1
for pos, item in enumerate(max_count):
    if item == max(max_count):
        print(pos)
        break
