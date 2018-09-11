# https://www.hackerrank.com/contests/pythonist3/challenges/capitalize

def capitalize(s):
    l = list(s)
    for i in range(len(l)):
        if l[i].isalpha():
            if i == 0 or l[i-1] == ' ':
                l[i] = l[i].upper()

    return ''.join(l)
s = input()
print(capitalize(s))
