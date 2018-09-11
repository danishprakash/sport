n = int(input())
a = [int(x) for x in input().split()]
for i in range(n):
    key = a[i]
    j = i-1
    while j >= 0 and key <= a[j]:
       a[j+1] = a[j]
       j -= 1
       flag = 1
       #print(' '.join([str(x) for x in a]))
    a[j+1] = key
    print(' '.join([str(x) for x in a]))


