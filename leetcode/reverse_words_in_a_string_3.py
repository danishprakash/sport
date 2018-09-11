def reverseWords(s):
    l1 = s.split(" ")
    res = []
    for item in l1:
        temp = []
        temp = list(item)
        temp = temp[::-1]
        res.append(''.join(temp))
    return ' '.join(res)

print(reverseWords("Let's take LeetCode contest"))
