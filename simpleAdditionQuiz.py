# Math game quiz
# prompts users to answer simple addition problems using random numbers from 0-100
# added subtraction, multiplication, and division

import random
def calculateAverage():
	sum = num1 + num2
	return sum

counter = 0

while True:
	num1 = random.randrange(0,100)
	num2 = random.randrange(0,100)
	average = calculateAverage()
	userInput = input("What is the answer to %i + %i or press (done) to quit:" %(num1,num2))
	userInput = userInput.lower()	
	
	if userInput == "done":
		print("Good-Bye")
		break 
	
	try: 
		userInput = int(userInput)
	except:
		userInput = input("Bad input Please enter an integer only:")
	
	if userInput == average:
		counter += 1
		print("The answer is %i" %(average))
		print("Good Job! Your score is %i" %(counter))
	elif userInput != average:
		print("Wrong Answer You got 0 points for this question")
		print("The right answer is %i" %(average))

		
	
	



	
	

