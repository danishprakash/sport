t = int(input())

for i in range(t):
    orig = input()
    old = input()
    new = input()
    res = orig
    j = 0

    while j < len(res):
        #print(j, orig[j:j+len(old)])
        if res[j:j+len(old)] == old:
            #print(orig[j:len(old)], len(old), j)
            res  = res[:j] + new + res[j+len(old):]
        #print(res)
        j += 1

    print(res)
