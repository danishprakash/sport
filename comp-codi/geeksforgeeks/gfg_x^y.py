import math
t = int(input())

for i in range(t):
    n = int(input())
    fact = 2
    flag = 0
    while fact <= int(math.sqrt(n)):
        temp = n
        while temp > 1:
            #print(temp)
            if temp%fact == 0:
                temp = int(temp/fact)
            else:
                fact += 1
                break
        if temp == 1:
            flag = 1
            break

    if flag == 1 and fact <= math.sqrt(n):
        print(1)
    else:
        print(0)

