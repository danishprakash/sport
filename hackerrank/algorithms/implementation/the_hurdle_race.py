# https://www.hackerrank.com/challenges/the-hurdle-race/problem

n, k = [int(x) for x in input().split()]
s = [int(x) for x in input().split()]


def soln(s, k):
    return 0 if max(s) <= k else (max(s)-k)


print(soln(s, k))

