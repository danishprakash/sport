# http://practice.geeksforgeeks.org/problems/remove-common-characters-and-concatenate/0

t = int(input())

for i in range(t):
    s1 = list(input())
    s2 = list(input())
    f1 = []
    f2 = []
    j = 0
    while j < len(s2):
        k = 0
        while k < len(s1):
            if s2[j] == s1[k]:
                f1.append(s2[j])
                s2[j] = ''
                s1[k] = ''
            k += 1
        j += 1
    res = s1 + s2
    j = 0
    res1 = []
    while j < len(res):
        if res[j] not in f1:
            res1.append(res[j])
        j += 1
    print(''.join(res1)) if res1 != [] else print(-1)
