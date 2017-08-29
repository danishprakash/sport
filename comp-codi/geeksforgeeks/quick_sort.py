# Implementation of quick sort in python

def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q+1, r)
    return ' '.join([str(x) for x in a])

def partition(a, p, r):
    x = a[r]
    i = p-1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
    temp = a[i+1]
    a[i+1] = a[r]
    a[r] = temp
    return i+1

a = [int(x) for x in input().split()]
print(quicksort(a, 0, len(a)-1))
