def dec_to_bin(n):
    l = list()
    while n >= 1 and n < 10**6:
        if (n%10)%2 == 0:
            l.append(0)
            n /= 2
        else:
            l.append(1)
            n -= 1
            n /= 2
        #print(n)
    return(''.join(str(x) for x in l[::-1]))

t = int(input())

for i in range(t):
    count = 0
    n = int(input())
    for j in range(1, n+1):
        #print(j)
        temp = dec_to_bin(j)
        #print(temp)
        for item in temp:
            if item == '1':
                count += 1
    print(count)
