# http://practice.geeksforgeeks.org/problems/transform-the-array/0

t = int(input())

for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    zero_count = 0
    i = 0
    a = []
    for item in arr[:]:
        if item == 0:
            zero_count += 1
        else:
            a.append(item)
    j = 0
    while j < len(a)-1:
        if a[j] == a[j+1]:
            a[j] = 2 * a[j]
            del a[j+1]
            zero_count += 1
            continue
        j += 1

    print(' '.join([str(x) for x in a]), end=' ')
    [print(0, end=' ') for x in range(zero_count)]
    print()
