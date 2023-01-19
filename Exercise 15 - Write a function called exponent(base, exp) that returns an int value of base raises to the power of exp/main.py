#Exercise from https://pynative.com/python-basic-exercise-for-beginners/
#Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

def exponent(base, exp):
  if (exp==1):
    return(base)
  if(exp!=1):
    return(base*exponent(base, exp - 1))
base = int(input("Enter base value: "))
exp = int(input("Enter exponential value: "))
print("Result is: ", exponent(base, exp))
