# https://leetcode.com/problems/arranging-coins

n = int(input())
steps = 0
csteps = 0
for i in range(1, n):
    steps += i
    if steps >= n:
        if i == csteps:
            print(i)
        else:
            print(i-1)
        break
    csteps = (n-steps)

