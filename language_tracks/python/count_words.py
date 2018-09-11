#!python3
#simple python script to count the number of words in a given string from the clipboard

import pyperclip

text = pyperclip.paste()
text = text.split(' ')

count = 0

for item in text:
    if len(item) > 2:               #change the min word lenght to be counter
        count += 1

pyperclip.copy(str(count))          #result copied to clipboard
