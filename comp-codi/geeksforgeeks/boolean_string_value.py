# http://practice.geeksforgeeks.org/problems/boolean-string-value

t = int(input())
for i in range(t):
    a = list(input())
    j = 0
    while len(a) > 1:
        if a[1] == 'A':
            res = int(a[0]) and int(a[2])
        elif a[1] == 'B':
            res = int(a[0]) or int(a[2])
        elif a[1] == 'C':
            res = int(a[0]) ^ int(a[2])
        a.remove(a[2])
        a.remove(a[1])
        a[0] = res
        j = 0
    print(''.join([str(x) for x in a]))


