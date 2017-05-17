import math
t = int(input())

for i in range(t):
    sum_ = 0
    n = input()
    for item in n:
        sum_ += math.factorial(int(item))
    if sum_ == int(n):
        print(1)
    else:
        print(0)
