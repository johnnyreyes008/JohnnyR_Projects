tax_rate = 0.20 #tax rate the user will be charged
standard_deduction = 10000 #the deduction the user will be deducted 
dependent_deduction = 3000 #additional deduction per dependent

gross_income = float(input("Enter the gross income: ")) #aquires the gross income from user
total_dependents = int(input("Enter the number of dependents:")) #aquire totsl dependents from user

taxable_income = gross_income - standard_deduction - dependent_deduction * total_dependents
#calculates the taxable income 

income_tax = taxable_income * tax_rate #calculates the come tax

print("The income tax is $", income_tax) #prints the income tax to the user