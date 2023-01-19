#Exercise from https://pynative.com/python-input-and-output-exercise/
#Exercise 18 - Convert Decimal number to octal using print() output formatting
#Given: num = 8
#Expected output:
#The octal number of decimal number 8 is 10

dec = input("Write a decimal number: ")
octal = oct(int(dec))

print("The octal number of decimal number", dec, "is", octal)
