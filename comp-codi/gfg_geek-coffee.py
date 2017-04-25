#http://practice.geeksforgeeks.org/problems/geek-and-coffee-shop/0

t = int(input())
for i in range(t):
    n, m = [int(x) for x in input().split()]
    j=0
    while round(n)>=0:
        j+=1
        n /= 2
        if j+1==m:
            print(round(n))
            break
