# http://practice.geeksforgeeks.org/problems/second-most-repeated-string-in-a-sequence

t = int(input())

for i in range(t):
    n = int(input())
    seq = input().split()
    d = {}
    for item in seq:
        if item not in d.keys():
            d[item] = 0
        else:
            d[item] += 1
    del d[max(d, key=d.get)]
    print(max(d, key=d.get))
