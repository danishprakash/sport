sentence = str(input())
sentence = sentence.split()
res = []

for word in sentence:
    res.append(''.join(list(word)[::-1]))

print(' '.join(res))
