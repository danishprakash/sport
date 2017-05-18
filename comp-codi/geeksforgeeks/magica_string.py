t = int(input())

for i in range(t):
    n = input()
    dic = dict()
    dic2 = dict()
    inc = 25
    s = ''
    for i in range(97, 110):
        dic[i] = i+inc
        inc -= 2
    inc2 = 1
    for j in range(110, 123):
        dic2[j] = j-inc2
        inc2 += 2
    for item in n:
        if ord(item) in dic.keys():
            s += chr(dic[ord(item)])
        elif ord(item) in dic2.keys():
            s += chr(dic2[ord(item)])
    print(s)

