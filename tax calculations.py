# input statements
salary = float(input("Enter your salary: $"))
numDependents = float(input("Enter the number of dependents: "))

# calculate taxes here
stateTax = (salary * 0.065)
federalTax = (salary * 0.28)
dependentDeductions = ( numDependents * salary * 0.025)
totalWithholding = stateTax + federalTax + dependentDeductions
takeHomePay = (salary - totalWithholding)

# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeductions))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
