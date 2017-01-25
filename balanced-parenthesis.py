exp = raw_input("Enter expression to be checked for balanced parenthesis: ")
counter = 0
for char in exp:
	if char == '(':
		counter += 1
	elif char == ')':
		counter -= 1
if counter == 0:
	print("Entered string has balanced parenthesis")
else:
	print("Entered string does not have balanced parenthesis")
