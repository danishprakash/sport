n = int(input())
#print(n)
for i in range(n):
    n, m = [int(s) for s in input().split()]
    #print(n, m)
    squares = 0
    squares += ((n-1) * (m-1))  #basic left to right top to bottom squares
    squares += 2*((n-2)*(m-2))    #semi full left to right top to bottom squares
    #squares +=

    if n == m:
        squares += 1 + (n/2)

    print("Case #" + str(i+1) + ": " + str((squares)%(pow(10,9)+7)))
    print(pow(10,9)+7)
