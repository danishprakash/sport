n = int(input())
l = list()
while n >= 1:
    if (n%10)%2 == 0:
        l.append(0)
        n /= 2
    else:
        l.append(1)
        n -= 1
        n /= 2
    print(n)
print(''.join(str(x) for x in l[::-1]))
