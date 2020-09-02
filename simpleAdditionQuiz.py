# Math game quiz
# prompts users to answer simple addition problems using random numbers from 0-100
# added subtraction, multiplication, and division

def printBanner():
	print("\t\t\t #####################      ")
	print("\t\t\t       Math Quiz       	 ")
	print("\t\t\t  By Falconscrest123        ")
	print("\t\t\t #####################\n\n\n") 

def calculateAverage():
	sum = num1 + num2
	return sum
	
def calculateDiffernce():
	difference = num1 - num2
	return difference
	
def multiplyNumber():
	product = num1 * num2
	return product

def divideNumber():
	divide = float(num1 / num2)
	divide = round(divide, 2)
	return divide
	
	
import random
printBanner()
counter = 0

while True:
	num1 = random.randrange(0,100)
	num2 = random.randrange(0,100)
	
	quizType = input("Do you want to add,subtract,multiply or divide:")
	quizType = quizType.lower()
	
	if quizType == "add" or quizType == "addition":
		answer = calculateAverage()
		userInput = input("What is the answer to %i + %i or press (done) to quit:" %(num1,num2))
		userInput = userInput.lower()
	elif quizType == "subtract" or quizType == "subtraction":
		answer = calculateDiffernce()
		userInput = input("What is the answer to %i - %i or press (done) to quit:" %(num1,num2))
		userInput = userInput.lower()
	elif quizType == "multiply" or quizType == "multiplication":
		answer = multiplyNumber()
		userInput = input("What is the answer to %i * %i or press (done) to quit:" %(num1,num2))
		userInput = userInput.lower()
	elif quizType == "divide" or quizType == "division":
		answer = divideNumber()
		userInput = input("What is the answer to %i / %i or press (done) to quit:" %(num1,num2))
		userInput = userInput.lower()
	else:
		print("Invalid input")
		continue
	
	if userInput == "done":
		print("Good-Bye")
		break 
	
	try: 
		userInput = float(userInput)
	except:
		userInput = input("Bad input Please enter an integer only:")
	
	if userInput == answer:
		counter += 1
		print("\nThe answer is %4.2f" %(answer))
		print("Good Job! Your score is %i\n" %(counter))
	elif userInput != answer:
		print("Wrong Answer You got 0 points for this question")
		print("The right answer is %4.2f" %(answer)
