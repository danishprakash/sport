# http://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/

a = list(map(int, input().split()))

currentSum = 0
maxLen = 0
d = {}

for i in range(len(a)):
    currentSum += a[i]
    
    print('-->', end='')
    print(currentSum, a[i])
    if i == 0 and a[i] == 0:
        maxLen = 1

    if currentSum == 0:
        maxLen += 1

    if currentSum in d:
        print(currentSum, d[currentSum],(i-d[currentSum]), maxLen)
        maxLen = max(maxLen, i-d[currentSum])
    else:
        d[currentSum] = i

print(maxLen)
