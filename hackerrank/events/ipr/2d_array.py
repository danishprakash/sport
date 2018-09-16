# https://www.hackerrank.com/challenges/2d-array

arr = list()
max_sum = -999

for line in range(6):
    arr.append([int(x) for x in input().split()])

for i in range(4):
    for j in range(4):
        sum_ = sum([arr[i][j],
                    arr[i][j+1],
                    arr[i][j+2],
                    arr[i+1][j+1],
                    arr[i+2][j],
                    arr[i+2][j+1],
                    arr[i+2][j+2]])

        if sum_ > max_sum:
            max_sum = sum_

print(max_sum)
