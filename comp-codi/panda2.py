t = int(input())
squares = 0
for i in range(t):
    n, m = [int(x) for x in input().split()]
    k = 0

    while n >= 1 or m >= 1:
        #print(n, m)
        n -= 1
        m -= 1
        k += 1
        squares += k*m*n
    #if n == m:
        #squares += 1
    #print(squares)
    print("Case #" + str(i+1) + ": " + str((squares)%(pow(10,9)+7)))
    #print(pow(10,9)+7)
