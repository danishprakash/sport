# https://leetcode.com/problems/jewels-and-stones/description/

j = input()
s = input()

count = 0

for i in range(1, len(s)-1):
    if s[i] in list(j): count += 1

print(count)

# one-liner
# len([x for x in s if x in j])

