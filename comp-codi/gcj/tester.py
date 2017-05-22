n, m =  [int(x) for x in input().split()]
a =  [int(x) for x in input().split()]
b =  [int(x) for x in input().split()]

counter = countera = counterb = 0
i = 1
flag = False

while(i <= max(max(a), max(b))):
    flag = False
    for item in a:
        if i % item == 0:
            countera += 1
        if countera == len(a):
            flag = True

    for item in b:
        if item % i == 0:
            counterb += 1
        if counterb == len(b):
            flag = True

    if flag == True:
        counter += 1
    i += 1
    countera = counterb = 0

print(counter)
