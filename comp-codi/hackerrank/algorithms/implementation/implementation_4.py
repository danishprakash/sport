n, m =  [int(x) for x in input().split()]
a =  [int(x) for x in input().split()]
b =  [int(x) for x in input().split()]

counter = 0
flag = False
i = 1

while(i <= max(max(a), max(b))):
    flag = False
    counterb = countera = 0

    for item in a:
        if i % item == 0:
            countera += 1

    if countera == len(a):
        for item in b:
            if item % i == 0:
                counterb += 1

        if counterb == len(b):
            counter += 1

    i += 1

print(counter)
