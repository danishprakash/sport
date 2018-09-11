def bestAverage(scores):
    d_sum = {}
    d_count = {}

    for i in range(n):
        if scores[i][0] not in d_sum.keys():
            d_sum[scores[i][0]] = int(scores[i][1])
            d_count[scores[i][0]] = 1
        else:
            d_sum[scores[i][0]] += int(scores[i][1])
            d_count[scores[i][0]] += 1

    res = []
    for name, marks in d_sum.items():
        res.append(marks//d_count[name])

    return max(res) if res != [] else 0

n = int(input())
m = int(input())
scores = []

for i in range(n):
    score = input().split()
    scores.append(score)

print(bestAverage(scores))
