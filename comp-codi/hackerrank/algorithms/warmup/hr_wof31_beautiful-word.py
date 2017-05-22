#!/bin/python3

import sys

w = input().strip()
flag = 0

for i in range(len(w)-1):
    if w[i] == w[i+1] or (w[i] in ['a', 'e', 'i', 'o', 'u', 'y'] and w[i+1] in ['a', 'e', 'i', 'o', 'u', 'y']):
        flag = 1
        break
        
if flag == 1:
    print('No')
else:
    print('Yes')
    
# Print 'Yes' if the word is beautiful or 'No' if it is not.