import re

a = "GeekForGeeks"
b = "Gks"
alen = len(a)
blen = len(b)

for i in range(alen):
    for j in range(blen):
        if a[i] != b[i]:
            
