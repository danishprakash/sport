t = int(input())

for i in range(t):
    n = input()
    dic = dict()
    dic2 = dict()
    inc, inc2 = [25, 1]
    s = ''
    for i in range(97, 123):
        if i < 110:
            dic[i] = i+inc
            inc -= 2
        elif i > 109:
            dic2[i] = i-inc2
            inc2 += 2
    for item in n:
        if ord(item) in dic.keys():
            s += chr(dic[ord(item)])
        elif ord(item) in dic2.keys():
            s += chr(dic2[ord(item)])
    print(s)

