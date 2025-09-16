print("Number Guessing Game")
startRange = int(input("Enter Starting Range of Number:"))
endRange = int(input("Enter Ending Range of Number:"))

print(f"Think a Number Between {startRange} and {endRange}, I will Try to guess it")

def GuessNum(startRange,endRange):
	if startRange > endRange:
		return True

	mid = (startRange + endRange)//2

	print(f"Is the Number {mid}? (Y/N): ",end="")
	user = input().strip()

	if user in ("Y","y"):
		print("Congrats, Successfully guessed the number.")
		return False

	elif user in ("N","n"):
		print(f"Is Number Greater than {mid}? (Y/N):",end="")
		user = input().strip()

		if user in ("Y","y"):
			return GuessNum(mid + 1,endRange)
		elif user in ("N","n"):
			return GuessNum(startRange, mid - 1)
		else:
			print("Invalid Input,Please enter Y or N:")
			return GuessNum(startRange,endRange)
	else:
		print("Invalid Input,Please enter Y or N:")
		return GuessNum(startRange,endRange)

GuessNum(startRange,endRange)
