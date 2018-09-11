# https://leetcode.com/problems/arranging-coins
# Concept: https://discuss.leetcode.com/topic/65655/c-1-line-code

def arrangeCoins(n):
    return int((-0.5 + ((2*n)+0.25)**(.5)))

n = int(input())
print(arrangeCoins(n))

