t = int(input())

for i in range(t):
    s = input()
    k = int(input())
    if k >= len(s)-1:
        print('0')
        continue
    fval = 5000
    for i in range(len(s)-k+1):
        a = s[0:i]+s[i+k:]
        minVal = 0
        temp = []
        #print(a)
        for j in range(len(a)):
            if a[j] not in temp:
                minVal += (a.count(a[j])**2)
                temp.append(a[j])
            #print(minVal)
        if minVal < fval:
            fval = minVal
    print(fval)
