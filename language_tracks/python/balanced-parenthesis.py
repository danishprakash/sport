#A balance parenthesis algorithm based on the number of parentheses. 
#Counter =0, subsequent number of ( will increment the counter and)  will 
#decrement the counter. In the end if counter == 0 then the expression has 
#balanced parentheses.

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
