#http://practice.geeksforgeeks.org/problems/check-if-the-door-is-open-or-closed/0

t = int(input())

for i in range(t):
    n = int(input())
    doors = list()
    for item in range(n):
        doors.append(0)
    for j in range(n):
        for k in range(len(doors)):
            if (k+1)%(j+1) == 0:
                doors[k] = not doors[k]
    doors = [str(int(x)) for x in doors]
    print((''.join(doors)))

