s = input()
news = s
i = 0
while i < len(s) and i >= 0:
    if len(s) == 2 and i == 1:
        i -= 1
    elif i+1 == len(s):
        break
    if s[i] == s[i+1]:
        news = news[:i] + news[i+2:]
    s = news
    if s == '':
        print('Empty String')
        break
    if i == len(s):
        break
    if s[i] == s[i-1] and i > 0:
        i -= 1
    else:
        i += 1
    #print(s, len(s), i)

print(s)
