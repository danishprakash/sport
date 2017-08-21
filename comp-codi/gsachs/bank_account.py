# https://www.hackerrank.com/contests/gs-codesprint/challenges/bank-accounts

t = int(input())
for j in range(t):
    n, k, x, d = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]
    for i in range(n):
        sum_ += max(k, ((x/100)*p[i]))
    if sum_ > d:
        print('upfront')
    else:
        print('fee')

