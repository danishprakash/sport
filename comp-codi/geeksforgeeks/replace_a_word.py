t = int(input())

for i in range(t):
    orig = input()
    old = input()
    new = input()
    res = orig
    
    for j in range(len(orig)):
        print(j, orig[j:j+len(old)])
        if orig[j:j+len(old)] == old:
            print(orig[j:len(old)], len(old), j)
            res  = orig[:j] + new + orig[len(old):]

    print(res)
