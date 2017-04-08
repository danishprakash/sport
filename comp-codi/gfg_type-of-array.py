n = int(input())

for j in range(n):
    s = int(input())
    a = [int(x) for x in input().split()]
    aflag = dflag = 0
    for i in range(s):
        if i == 0:
            continue
        if a[i] >= a[i-1]:
            aflag += 1
            print(aflag, dflag)
            continue
        else:
            aflag -= 1
        if a[i] <= a[i-1]:
            dflag += 1
        else:
            dflag -= 1

        print(aflag, dflag)

    if aflag == s-1:
        print(max(a), '1')
    elif dflag == s-1:
        print(max(a), '2')
    elif dflag > aflag and dflag != 0:
        print(max(a), '3')
    elif aflag > dflag and aflag != 0:
        print(max(a), '4')
