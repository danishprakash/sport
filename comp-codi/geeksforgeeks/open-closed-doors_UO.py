#http://practice.geeksforgeeks.org/problems/check-if-the-door-is-open-or-closed/0

t = int(input())

for i in range(t):
    n = int(input())
    doors = [0 for i in range(n)]
    for j in range(n):
        for k in range(n):
            if (k+1)%(j+1) == 0:
                doors[k] = not doors[k]
    doors = [str(int(x)) for x in doors]
    print((' '.join(doors)))

