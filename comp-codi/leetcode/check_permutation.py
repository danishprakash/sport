# https://leetcode.com/problems/permutation-in-string/description/

def checkInclusion(s1, s2):
    c1 = [0] * 26
    for i in range(len(s1)):
        c1[ord(s1[i]) - ord('a')] += 1
    print(c1)
    for i in range(len(s2)-len(s1)+1):
        # print(s1, s2[i:i+len(s1)])
        c2 = [0] * 26
        for j in range(len(s1)):
            c2[ord(s2[i+j]) - ord('a')] += 1
        if c1 == c2:
            return True
    return False

print(checkInclusion('adc', 'dcda'))

