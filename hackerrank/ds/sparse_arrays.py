# https://www.hackerrank.com/challenges/sparse-arrays/problem

n = int(input())
strings = [input() for i in range(n)]
q = int(input())
queries = [input() for i in range(q)]

res = [0] * q

for i in range(len(queries)):
    for string in strings:
        if queries[i] == string:
            res[i] += 1

for item in res: print(item)
