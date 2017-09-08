# https://leetcode.com/problems/plus-one

def plusOne(a):
    return list(map(int, str(int(''.join([str(x) for x in a]))+1)))

print(plusOne([int(x) for x in input().split()]))
