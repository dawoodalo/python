first = float(input(" please enter a number "))
second = float(input(" please enter a second number "))
operation = input("	Choose the operation (+, -, /, *):  ")
if operation=="+" :
	three=first + second
	print ( "The answer is %s. " % (three))
elif operation == "-":
	three = first - second
	print ( "The answer is %s. " % (three))
elif operation == "/":
	three = first / second
	print ( "The answer is %s. " % (three))
elif operation == "*":
	three = first * second
	print ( "The answer is %s. " % (three))
else: 
	print(" The operation is not valid.")
