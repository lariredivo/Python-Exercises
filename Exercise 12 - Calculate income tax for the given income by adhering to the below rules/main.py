#Exercise from https://pynative.com/python-basic-exercise-for-beginners/
#Exercise 12: Calculate income tax for the given income by adhering to the below rules
#First $10,000 -> rate 0%
#Next $10,000 -> rate 10%
#The remaining -> rate 20%

#Expected Output:

#For example, suppose the taxable income is 45000 the income tax payable is 10000*0% + 10000*10%  + 25000*20% = $6000.

tax_income = 45000
tax_payable = 0
print("Given income", tax_income)

if tax_income <= 10000:
  tax_payable = 0
elif tax_income <= 20000:
  x = tax_income - 10000
  tax_payable = x * 10/100
else:
  tax_payable = 0
  tax_payable = 10000 * 10 / 100
  tax_payable += (tax_income - 20000) * 20 / 100
  
print("Total tax pay is", tax_payable)
