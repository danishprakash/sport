# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem<Paste>


def height_list(word): return max([s[ord(x)-97] for x in word]) * len(word)


s = [int(x) for x in input().split()]
print(height_list(input()))
