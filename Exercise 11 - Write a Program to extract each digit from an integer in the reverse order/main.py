#Exercise from https://pynative.com/python-basic-exercise-for-beginners/
#Write a Program to extract each digit from an integer in the reverse order
#For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

number = input("Write a number: ")

number_to_string = str(number)
reverse_number = "".join(reversed(number_to_string)) 

for i in reverse_number:
        reverse_number=reverse_number.replace(i," "+i+" ")

print(reverse_number)
