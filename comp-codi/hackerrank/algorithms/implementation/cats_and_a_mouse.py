# https://www.hackerrank.com/challenges/cats-and-a-mouse

t = int(input())
for i in range(t):
    a, b, m = [int(x) for x in input().split()]
    if abs(a-m) < abs(b-m):
        print('Cat A')
    elif abs(a-m) > abs(b-m):
        print('Cat B')
    else:
        print('Mouse C')
