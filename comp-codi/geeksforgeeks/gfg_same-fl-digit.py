#http://practice.geeksforgeeks.org/problems/numbers-with-same-first-and-last-digit/0
import math

t = int(input())

for i in range(t):
    l, r = [int(x) for x in input().split()]
    count = 0
    for item in range(l,r):
        if round(item/(10**(len(str(item))-1))) == round(item%10):
            count += 1
            #print(item)
            #print(math.floor(item/(10**(len(str(item))-1))), math.floor(item%10))
        #print(item)
    print(count)
