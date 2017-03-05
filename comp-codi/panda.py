n = int(input())
#print(n)
for i in range(n):
    n, m = [int(s) for s in input().split()]
    #print(n, m)
    squares = 0                         #counter for squares
    squares += ((n-1) * (m-1))          #basic left to right top to bottom squares
    squares += 2*((n-2)*(m-2))          #semi-full left to right top to bottom squares + 1x1 diagonal squares
    if m>=3 or n>=3 and n==m:           #diagonal long squares
        squares += (m-2)

    if n == m and (m>2 or n>2):
        squares += 1                    #one big outer square

    print("Case #" + str(i+1) + ": " + str((squares)%(pow(10,9)+7)))
    print(pow(10,9)+7)
