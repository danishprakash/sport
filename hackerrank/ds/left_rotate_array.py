# https://www.hackerrank.com/challenges/linkedin-practice-array-left-rotation

n, m = [int(x) for x in input().split()]
a = list(map(int, input().split()))

def lrotate(a, m):
    return a[m:] + a[:m]

a = lrotate(a, m)
print(' '.join(list(map(str, a))))
