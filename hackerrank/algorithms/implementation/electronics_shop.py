# https://www.hackerrank.com/challenges/electronics-shop

s, k, u = [int(x) for x in input().split()]
key = [int(x) for x in input().split()]
usb = [int(x) for x in input().split()]
max_ = -1

for i in range(k):
    for j in range(u):
        if key[i]+usb[j] > s:
            continue
        if key[i]+usb[j] > max_:
            max_ = key[i]+usb[j]
print(max_)


