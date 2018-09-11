# https://www.hackerrank.com/contests/gs-codesprint/challenges/buy-maximum-stocks

n = int(input())
s = [int(x) for x in input().split()]
m = int(input())
max_ = 0
count = 0
flag = 0
for i in range(n):
    max_ += s[i]*(i+1)
    count += (i+1)
    if max_ > m:
        while max_ > m:
            max_ -= s[i]
            count -= 1
    print(max_)

print(count)

