<<<<<<< HEAD:comp-codi/gfg_geek-coffee.py
# http://practice.geeksforgeeks.org/problems/geek-and-coffee-shop/0
=======
#http://practice.geeksforgeeks.org/problems/geek-and-coffee-shop/0
import math
>>>>>>> ad33d4e14cd07ac36f9a022ccbb6c171defc6a74:comp-codi/geeksforgeeks/gfg_geek-coffee.py

t = int(input())
for i in range(t):
    n, m = [int(x) for x in input().split()]
    j=0
    res=0
    if m==1:
        res=n
    while n>0:
        j+=1
        n = math.floor(n/2)
        if j+1==m:
            res=math.floor(n)
            break
    print(res)
