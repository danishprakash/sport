# https://www.hackerrank.com/challenges/counting-valleys/problem

n = int(input())
steps = input()

level = 0
count = 0
previous_step = ""

for step in steps:
    if step == "D": level -= 1
    else: level += 1
    if level == 0 and step == "U": count += 1
    previous_step = step

print(count)
