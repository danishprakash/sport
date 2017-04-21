t = int(input())
s = input()
k = int(input())


for i in range(t):
    min_ = 2500
    for i in range(len(s)-k+1):
        a = s[0:i]+s[i+k:]
        temp = []
        #print(a)
        minVal = 0
        for j in range(len(a)):
            if a[j] not in temp:
                minVal += (a.count(a[j])**2)
                temp.append(a[j])
            print(minVal)
        if minVal < min_:
            min_ = minVal
    if min_ == 2500:
        print('0')
    else:
        print(min_)
