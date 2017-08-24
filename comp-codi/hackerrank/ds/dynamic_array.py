# https://www.hackerrank.com/challenges/dynamic-array

n, q = [int(x) for x in input().split()]
s = [[] for x in range(n)]
lastAnswer = 0
for i in range(q):
    t, x, y = [int(x) for x in input().split()]
    ls = []
    if t == 1:
        s[(x^lastAnswer)%n].append(y)
    elif t == 2:
        seq = s[(x^lastAnswer)%n]
        lastAnswer = seq[y%len(seq)]
        print(lastAnswer)
