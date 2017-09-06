n = int(input())
d = dict()
for i in range(n):
    a, b = input().split()
    d[a] = b
for i in range(n):
    test = input()
    if test in d.keys():
        print(str(test)+'='+str(d[test]))
    else:
        print('Not found')
