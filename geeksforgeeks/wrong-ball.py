t = int(input())

for i in range(t):
    b = input()
    count = 0
    for j in range(len(b)):
        if b[j] == "R" and (j+1)%2 == 0:
            count += 1
        if b[j] == "B" and (j+1)%2 != 0:
            count += 1 
    print(count)
