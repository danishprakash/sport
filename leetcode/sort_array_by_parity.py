# https://leetcode.com/problems/sort-array-by-parity/description/

def solution(A):
    return [x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1]
