def detectCapital(s):
    flag = 0
    aflag = 0
    if s.isupper():
        return True
    for i in range(len(s)):
        if s[i].isupper():
            if i == 0:
                aflag = 1
            elif aflag == 1:
                return False
            flag += 1
        else:
            flag -= 1
    if (aflag == 1 and abs(flag) == len(s)-2):
        return True
    else:
        return False


s = input()
print(detectCapital(s))
