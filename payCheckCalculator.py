# Calculates paycheck using hours and hourly wage

def printBanner():
	print("\t\t\t #####################      ")
	print("\t\t\t Paycheck Calculator        ")
	print("\t\t\t  By Falconscrest123        ")
	print("\t\t\t #####################\n\n\n")    

def calculatePay():
	total = 0
	regHours = 40
	if hours > 40:
		overtimeHours = hours - regHours
		overtimeWage = hourlyWage * 1.5
		total = (regHours * hourlyWage) + (overtimeHours * overtimeWage) 
	elif hours <= 40:
		total = hours * hourlyWage
	return total

def calculate401k(deductPercent):
	taxIncome = 0
	retireCont = 0
	totalPay = calculatePay()
	retireCont = totalPay * (deductPercent / 100)
	taxIncome = totalPay - retireCont
	return taxIncome, retireCont

def medicareTax(taxIncome):
	socSecTaxPerc = 0.062
	medTaxPerc = 0.0145
	socialSecurityTax = taxIncome * socSecTaxPerc
	medTax = taxIncome * medTaxPerc
	return socialSecurityTax, medTax
	
def incomeTax(taxIncome):
	fedTaxPerc = 0.0703
	maTaxPerc = 0.0462
	maIncomeTax = maTaxPerc * taxIncome
	fedIncomeTax = fedTaxPerc * taxIncome
	return maIncomeTax, fedIncomeTax

printBanner()	

while True:
	
	hours = input("Enter number of hours worked:")
	hourlyWage = input("Enter hourly wage:")
	deductPercent = input("Enter 401k contribution percentage:")
	
	try:
		hours = float(hours)
		hourlyWage = float(hourlyWage)
		deductPercent = int(deductPercent)
	except:
		print("Invalid data: Please try again")
		continue			
	
	taxIncome = calculatePay()
	
	if deductPercent == 0:
		socialSecurityTax, medTax = medicareTax(taxIncome)
		maIncomeTax, fedIncomeTax = incomeTax(taxIncome)
		finalGrossPay = taxIncome - socialSecurityTax - medTax - maIncomeTax - fedIncomeTax
		print("\nYour total pay is %4.2f" %(taxIncome))
		print("Medicare tax = %4.2f \nsocial Security Tax = %4.2f" %(socialSecurityTax,medTax))
		print("State(MA) income tax = %4.2f \nFederal income tax = %4.2f" %(maIncomeTax, fedIncomeTax))
		print("\nTake home money = %4.2f" %(finalGrossPay))  

	elif deductPercent > 0 or deductPercent < 100:
		socialSecurityTax, medTax = medicareTax(taxIncome)
		taxIncome, retireCont = calculate401k(deductPercent)
		maIncomeTax, fedIncomeTax = incomeTax(taxIncome)
		finalGrossPay = taxIncome - socialSecurityTax - medTax - maIncomeTax - fedIncomeTax
		print("\nYour total taxble income is %4.2f, and 401K contribution = %4.2f " %(taxIncome, retireCont))
		print("Medicare tax = %4.2f \nsocial Security Tax = %4.2f" %(socialSecurityTax,medTax))
		print("State(MA) income tax = %4.2f \nFederal income tax = %4.2f" %(maIncomeTax, fedIncomeTax))
		print("\nTake home money = %4.2f" %(finalGrossPay))  
 
	else:
		print("The precentage is not in range")
	print("\n")
	
	
	'''
	Bugs
	1) Try and Except function
	3) Negative numbers
	4) reduce repeated codes organize codes
	5) exit keyword to exit
	
	'''
