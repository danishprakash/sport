import re

t = int(input())

for i in range(t):
    s = input().split()
    hard, easy = [0, 0]
    for word in s:
        cons = re.findall(r'[bcdfghjklmnpqrstvwxyz]+', word, re.IGNORECASE)
        vows = re.findall(r'[aeiou]+', word, re.IGNORECASE)
        if len(cons) < 1:
            easy += 1
        elif len(max(cons)) > 3 or len(''.join(vows)) < len(''.join(cons)):
            hard += 1
        else:
            easy += 1

        #print(vows, cons)
    print(str((5*hard) + (3*easy)))
