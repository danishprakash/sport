n = int(input())
h = [int(x) for x in input().split()]
tallest = 0
count = 0
for i in range(n):
    if h[i] > tallest:
        tallest = h[i]
        count = 1
    elif h[i] == tallest:
        count += 1

print(count)
