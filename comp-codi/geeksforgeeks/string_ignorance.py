t = int(input())

for i in range(t):
    a = input()
    lst = {}
    for j in range(len(a)):
        #print(a[j], lst)
        if a[j].lower() not in lst:
            print(a[j], end='')
            lst[a[j].lower()] = 0
        elif a[j].lower() in lst:
            lst[a[j].lower()] += 1
            if lst[a[j].lower()] % 2 == 0:
                print(a[j], end='')


