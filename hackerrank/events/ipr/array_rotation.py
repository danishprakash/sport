# https://www.hackerrank.com/challenges/ctci-array-left-rotation

n, d = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(' '.join([str(x) for x in arr[d:] + arr[0:d]]))
