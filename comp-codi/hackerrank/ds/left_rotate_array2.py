# https://www.hackerrank.com/challenges/linkedin-practice-array-left-rotation

n, m = [int(x) for x in input().split()]
a = list(map(int, input().split()))

def lrotate(a):
    temp = a[0]
    for i in range(n-1):
        a[i] = a[i+1]
    a[-1] = temp

for i in range(m):
    lrotate(a)

print(' '.join(list(map(str, a))))
