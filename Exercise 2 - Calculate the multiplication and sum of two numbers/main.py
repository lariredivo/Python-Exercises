#Exercise from https://pynative.com/python-basic-exercise-for-beginners/
#Calculate the multiplication and sum of two numbers
#Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
number1 = 20
number2 = 30

if number1 * number2 <= 1000:
  result = number1 * number2
  print(f"The result is {result}")
else:
  result = number1 + number2
  print(f"The result is {result}")
  

